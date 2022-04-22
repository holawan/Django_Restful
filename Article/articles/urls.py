from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/',views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('cards/',views.card_list),
    path('cards/<int:card_pk>/' ,views.card_detail),
    path('<int:card_pk>/register/<int:article_pk>/', views.register),
]
