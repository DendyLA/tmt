from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Blog

def blog(request):
	blog = Blog.objects.all()

	return render(request, 'blog/blog.html', {'blog' : blog})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})