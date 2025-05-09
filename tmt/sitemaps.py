from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from about.models import ProjectImage
from blog.models import Blog
from main.models import News


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ['home', 'about', 'contact', 'news_list', 'blog']  # названия в urls.py

    def location(self, item):
        return reverse(item)


class ProjectImageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ProjectImage.objects.all()

    def location(self, obj):
        return reverse('gallery', args=[obj.pk])  # Только у изображений есть detail-страницы


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('blog_detail', args=[obj.pk])  # Вьюха принимает pk


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return News.objects.all()

    def location(self, obj):
        return reverse('news_detail', args=[obj.pk])
