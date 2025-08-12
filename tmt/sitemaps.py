from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.translation import override

from about.models import ProjectImage
from blog.models import Blog
from main.models import News
from opportunity.models import Tenders, Vacancies

LANGUAGES = ['en', 'ru', 'tk']

class StaticViewI18nSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return ['home', 'about', 'contact', 'news_list', 'blog']

    def location(self, item):
        with override(self.lang):
            return reverse(item)


class ProjectImageI18nSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return ProjectImage.objects.all()

    def location(self, obj):
        with override(self.lang):
            return reverse("gallery", args=[obj.pk])


class BlogI18nSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        with override(self.lang):
            return reverse("blog_detail", args=[obj.slug])


class NewsI18nSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return News.objects.all()

    def location(self, obj):
        with override(self.lang):
            return reverse("news_detail", args=[obj.slug])



class VacancyListI18nSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return ["vacancies"]  # name из urls.py

    def location(self, item):
        with override(self.lang):
            return reverse(item)


class VacancyI18nSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return Vacancies.objects.all()

    def location(self, obj):
        with override(self.lang):
            return reverse("vacancy_detail", args=[obj.slug])


class TenderListI18nSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return ["tenders"]  # name из urls.py

    def location(self, item):
        with override(self.lang):
            return reverse(item)


class TenderI18nSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def __init__(self, lang):
        self.lang = lang

    def items(self):
        return Tenders.objects.all()

    def location(self, obj):
        with override(self.lang):
            return reverse("tender_detail", args=[obj.slug])