from django.views.generic import DetailView, ListView

from .models import Post


class NewsList(ListView):
    model = Post
    template_name = "news.html"
    context_object_name = "posts"
    queryset = Post.objects.order_by('-created_at')


class PostDetail(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
