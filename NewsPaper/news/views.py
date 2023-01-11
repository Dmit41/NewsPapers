from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .models import News, Articles
from.filters import NewsFilter
from .forms import NewsForm


class NewsList(ListView):
    model = News
    ordering = '-date'
    template_name = 'all_news.html'
    context_object_name = 'all_news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'


class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class ArticleCreate(CreateView):
    form_class = NewsForm
    model = Articles
    template_name = 'article_edit.html'


class PostUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'update.html'


class PostDelete(DeleteView):
    model = News
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
