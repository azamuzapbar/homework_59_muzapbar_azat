from django.urls import path
from webapp.views import index_view
from webapp.articles import article_view
from webapp.articles import add_view


urlpatterns = [
    path('', index_view, name='index'),
    path('article/', index_view),
    path('article/<int:pk>', article_view, name='detailed_view'),
    path('article/add/', add_view, name='article_add')
]