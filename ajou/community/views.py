from community.models import Question
from django.shortcuts import render, redirect, get_object_or_404  # get_object_or_404 추가!
from .models import Post, Tag
from .forms import PostForm

def community_view(request):
    return render(request, 'community/community.html')

def ask_view(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'ask/ask.html', context)

def together_view(request):
    tag_name = request.GET.get('tag')
    if tag_name:
        posts = Post.objects.filter(tags__name=tag_name).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'tags': tags,
    }
    return render(request, 'together/together.html', context)

def together_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'together/detail.html', {'post': post})

def together_write_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username if request.user.is_authenticated else '익명'
            post.save()
            form.save_m2m()  # 기존 선택 태그 저장

            # 새로 입력한 태그 처리
            new_tags_str = request.POST.get('new_tags', '')
            if new_tags_str:
                new_tags_list = [tag.strip() for tag in new_tags_str.split(',') if tag.strip()]
                for tag_name in new_tags_list:
                    tag_obj, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag_obj)

            return redirect('together_page')
        else:
            print(form.errors)  # 폼 에러 출력
    else:
        form = PostForm()

    tags = Tag.objects.all()
    return render(request, 'together/write.html', {'form': form, 'tags': tags})

def ask_question_submit_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            Question.objects.create(title=title, content=content)
            return redirect('ask_page')
    return redirect('ask_page')
