# 메인 app의 urls.py / 각 url 로 라우팅

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # admin URL 연결
    path('chatbot/', include('chatbot.urls')), # chatbot 앱의 urls.py 로 연결
    path('', include('home.urls')), # home 앱의 urls.py 로 연결
]
