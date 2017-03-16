from .models import Post
from django.views.generic import DetailView


class PostView(DetailView):
    model = Post
    template_name = 'post_detail.html'
