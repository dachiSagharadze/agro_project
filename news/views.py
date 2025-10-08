from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer
from django.shortcuts import get_object_or_404

class NewsListApi(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NewsDetailApi(APIView):
    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        serializer = NewsSerializer(news, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
