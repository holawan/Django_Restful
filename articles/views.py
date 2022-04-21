from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Article
from .serializer import ArticleListSerializer, ArticleSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# @api_view()
#api_view내부에 아무것도 없으면 GET만 허용 
@api_view(['GET','POST'])
def article_list(request) :
    if request.method == 'GET' : 
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
    elif request.method == 'POST' :
        #데이터를 넣어야 하기 때문에 키워드 인자로 데이터를 넣는다.
        #첫번째 인자가 instance이기 때문에 data를 명시 
        serializer = ArticleSerializer(data=request.data)
        #유효성검사 통과하면 201 CREATED status 반환 
        #raise_exeption을 통해 else구문을 사용하지 않아도 유효성 검사를 통과하지 못하면, 400 에러 리턴 
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # #유효성 검사 통과 못하면 BAD REQUEST
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk) :
    article = get_object_or_404(Article,pk=article_pk)
    if request.method=='GET' :
        serializer = ArticleSerializer(article)

        return Response(serializer.data)
    elif request.method=='DELETE' :
        article.delete()
        #response에는 넘겨줄 값이 필요한데, 삭제는 이가 없으므로 직접 만들어줌
        data = {
            #pk는 url에서 가져온 article_pk이다. 
            'delete' : f'데이터 {article_pk}번이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT' :
        serializer = ArticleSerializer(article,data=request.data) 
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
