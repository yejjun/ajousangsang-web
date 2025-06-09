def notice_view(request):
    notifications = [
        {
            'date': '2025년 5월 30일',
            'projects': [
                {'title': 'Django 백엔드 개발자 모집', 'link': '#', 'status': '모집중'},
                {'title': '프론트엔드 UI/UX 디자이너 찾아요', 'link': '#', 'status': '모집중'},
            ]
        },
        {
            'date': '2025년 5월 29일',
            'projects': [
                {'title': '모바일 앱 개발팀 모집 (React Native)', 'link': '#', 'status': '모집중'},
                {'title': '데이터 분석가 구인', 'link': '#', 'status': '모집중'},
                {'title': '게임 기획자 모집', 'link': '#', 'status': '모집중'},
            ]
        },
        {
            'date': '2025년 5월 28일',
            'projects': [
                {'title': '오픈소스 프로젝트 팀원 구함', 'link': '#', 'status': '모집완료'},
            ]
        },
        # 더 많은 알림 데이터 추가 가능
    ]

    context = {
        'notifications': notifications,
        'page_title': '알림',  # 페이지 제목 추가 (헤더 등에서 사용 가능)
    }
    return render(request, 'notice/notice.html')


from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
