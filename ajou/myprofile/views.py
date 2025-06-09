
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage # staticfiles_storage 임포트

def myprofile_view(request):
    # 고정된 프로필 데이터
    user_profile_data = {
        'nickname': 'dust0924',
        'company_school': '아주대학교',
        'github_url': 'https://github.com/Munzzzzzi', # GitHub URL 추가
        'email': 'dust0924@ajou.ac.kr',
        'followers': 21,
        'following': 33,
        'profile_image_url': staticfiles_storage.url('img/yurim_profile.png'), # GitHub 프로필 이미지 경로
                                                                                # static/img/yurim_profile.png 에 이미지 넣어주세요.
        'participated_projects': [
            {'title': 'Django 기반 웹 서비스 개발', 'description': '사용자 인증 및 게시판 기능 구현', 'start_date': '2023-09-01', 'end_date': '2023-12-31'},
            {'title': '모바일 앱 UI/UX 디자인', 'description': '피그마를 이용한 프로토타이핑 및 사용자 테스트', 'start_date': '2024-01-10', 'end_date': '2024-04-01'},
            {'title': '데이터 분석 시각화 프로젝트', 'description': 'Python Matplotlib/Seaborn 활용 데이터 시각화', 'start_date': '2024-05-01', 'end_date': '진행 중'},
        ],
        'portfolio_images': [
            {'url': staticfiles_storage.url('img/portfolio/portfolio1.png')}, # static/img/portfolio/ 에 이미지 넣어주세요.
            {'url': staticfiles_storage.url('img/portfolio/portfolio2.png')},
            {'url': staticfiles_storage.url('img/portfolio/portfolio3.gif')},
            # 필요에 따라 더 많은 포트폴리오 이미지 추가
        ]
    }

    context = {
        'user_profile': user_profile_data,
    }

    return render(request, 'myprofile/myprofile.html', context)