from django.urls import path
from webapp.views import index_view
from webapp.articles import article_view
from webapp.articles import add_view


urlpatterns = [
    path('', index_view),
    path('article/', article_view),
    path('article/add/', add_view),
]