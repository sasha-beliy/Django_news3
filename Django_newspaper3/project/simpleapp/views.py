from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .filters import NewsFilter
from .models import News
from .forms import NewsForm


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'News.html'
    context_object_name = 'News'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = "Обновление ежедневно"
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'News.html'
    context_object_name = 'News'

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')



class ArticlesCreateView(CreateView):
    model = News
    fields = ['title', 'text', 'category']
    template_name = 'articles_form.html'


class ArticlesUpdateView(UpdateView):
    model = News
    fields = ['title', 'text', 'category']
    template_name = 'articles_edit.html'


class ArticlesDeleteView(DeleteView):
    model = News
    success_url = reverse_lazy('articles')
    template_name = 'articles_confirm_delete.html'