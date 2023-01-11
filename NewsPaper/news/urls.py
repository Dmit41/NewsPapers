from django.urls import path
from .views import (
   NewsList, NewsDetail, NewsCreate, ArticleCreate, PostUpdate, PostDelete, NewsListSearch
)


urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', NewsListSearch.as_view(), name='post_search')
]