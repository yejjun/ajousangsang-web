from community.models import Question


def community_view(request):
    return render(request, 'community/community.html')
def ask_view(request):
    questions = Question.objects.all()  # 데이터베이스에서 모든 질문 글을 가져옵니다.
    context = {'questions': questions}
    return render(request, 'ask/ask.html', context)
def together_view(request):
    return render(request, 'together/together.html')
def ask_question_submit_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            Question.objects.create(title=title, content=content)
            return redirect('ask_page')
        else:
            # 필요에 따라 에러 메시지 처리
            pass
    return redirect('ask_page')


from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
