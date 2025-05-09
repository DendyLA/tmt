"""
URL configuration for tmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main.views import main, subscribe, news_list, news_detail
from blog.views import blog, blog_detail
from contacts.views import contact


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, ProjectImageSitemap, BlogSitemap, NewsSitemap


sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectImageSitemap,
    'blog': BlogSitemap,
    'news': NewsSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
	path('', main , name='home'),
	path('subscribe/', subscribe, name='subscribe'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('about/', include('about.urls')),
    path('contact/', contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # В production используйте WhiteNoise для статических файлов
    urlpatterns += staticfiles_urlpatterns()