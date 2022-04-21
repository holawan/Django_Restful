from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from .models import Article
from .serializer import ArticleListSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

# @api_view()
#api_view내부에 아무것도 없으면 GET만 허용 
@api_view(['GET'])

def article_list(request) :
    #쿼리셋 조회
    # articles = Article.objects.all()
    #데이터가 없으면 404 리턴 
    articles = get_list_or_404(Article)
    # print(articles)   
    #직렬화하기 쿼리셋이니까 many=True
    serializer = ArticleListSerializer(articles,many=True)
    # print(serializer.data)
    #전체 데이터를 가져오는 것 
    return Response(serializer.data)

