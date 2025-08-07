from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from main.views import main, subscribe, news_list, news_detail
from blog.views import blog, blog_detail
from contacts.views import contact


from .sitemaps import (
    StaticViewI18nSitemap,
    ProjectImageI18nSitemap,
    BlogI18nSitemap,
    NewsI18nSitemap,
    LANGUAGES
)

# Инициализация sitemaps
sitemaps = {}
for lang in LANGUAGES:
    sitemaps[f'static-{lang}'] = StaticViewI18nSitemap(lang)
    sitemaps[f'projects-{lang}'] = ProjectImageI18nSitemap(lang)
    sitemaps[f'blogs-{lang}'] = BlogI18nSitemap(lang)
    sitemaps[f'news-{lang}'] = NewsI18nSitemap(lang)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

# URL с поддержкой i18n (будут иметь языковой префикс)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', main, name='home'),
    path('subscribe/', subscribe, name='subscribe'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('about/', include('about.urls')),
    path('contact/', contact, name='contact'),
    path('opportunities/', include('opportunity.urls'))
)

# Обработка медиафайлов в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()