# Create your views here.
# blog/views.py
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # Mengambil semua post yang sudah di-publish, diurutkan berdasarkan tanggal publish
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
