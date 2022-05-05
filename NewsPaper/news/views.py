from re import template
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    template_name = "news.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 10


class NewsSearch(ListView):
    model = Post
    template_name = "news.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context["search_enabled"] = True
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


class PostCreate(CreateView):
    template_name = "post_update.html"
    form_class = PostForm


class PostUpdate(UpdateView):
    template_name = "post_update.html"
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get("pk")
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = "post_delete.html"
    queryset = Post.objects.all()
    success_url = "/news/"
