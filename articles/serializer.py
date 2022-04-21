
from rest_framework import serializers
from .models import Article,Comment

class ArticleListSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Article
        fields = ('id','title')

class CommentSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer) :
    comment_set = CommentSerializer(many=True,read_only = True)
    #article.comment_set.count()를 가져오고 싶기 때문에 article이하를 source에 넣어줌 
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

