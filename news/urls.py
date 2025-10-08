from django.urls import path
from .views import NewsListApi, NewsDetailApi

urlpatterns = [
    path('', NewsListApi.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailApi.as_view(), name='news-detail'),
]
