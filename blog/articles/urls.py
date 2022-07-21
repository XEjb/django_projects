from django.contrib import admin
from django.urls import path, include
from .views import index, PostView, AuthorListView, AuthorDetailViews

urlpatterns = [
    path('', view=index),
    path('post', view=PostView.as_view()),
    path('authors', view=AuthorListView.as_view()),
    path('authors/<str:pk>', view=AuthorDetailViews.as_view())
]
