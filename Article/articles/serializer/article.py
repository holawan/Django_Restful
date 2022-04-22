
from rest_framework import serializers

from articles.serializer.card import CardSerializer
from ..models import Article
from .comment import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer) :
    comment_set = serializers.PrimaryKeyRelatedField(many=True,read_only = True)
    #article.comment_set.count()를 가져오고 싶기 때문에 article이하를 source에 넣어줌 
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    cards = CardSerializer(many=True,read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Article
        fields = ('id','title')