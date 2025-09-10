import os
from django.db import models
from django.utils.html import mark_safe
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields

from django.utils.translation import get_language
from parler.utils.context import switch_language

from django.utils.text import slugify

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    def __str__(self):
        return self.email


class Slogan(TranslatableModel):
    translations = TranslatedFields(
        first_title = models.CharField(max_length=100, verbose_name="Первый Заголовок", blank=True),
        second_title = models.CharField(max_length=100, verbose_name="Первый Заголовок", blank=True),
        third_title = models.CharField(max_length=100, verbose_name="Первый Заголовок", blank=True)
    )
    

    class Meta:
        verbose_name = "Слоган"
        verbose_name_plural = "Слоганы"
    
    def __str__(self):
        return self.first_title or 'No data'



class Services(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250, verbose_name='Заголовок', blank=True),
        text = models.TextField(verbose_name='Текст', blank=True)  
    )
   
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title or 'No data'


class News(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True),
        content = RichTextUploadingField(verbose_name='Текст', blank=True)
    )
     
    image = models.ImageField(upload_to='news_images/', verbose_name='Фото', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            current_lang = get_language()
            with switch_language(self, current_lang):
                title = self.safe_translation_getter('title', any_language=True)
            if title:
                base_slug = slugify(title)[:500]  # Ограничиваем длину
                slug = base_slug
                counter = 1
                while News.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                self.slug = slug

        if self.image:
            img = Image.open(self.image)

            if img.mode in ('RGBA', "P"):
                img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG', quality=70)

            output.seek(0)

            self.image = ContentFile(output.read(), os.path.basename(self.image.name))


        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title or 'No data'


class Slider(TranslatableModel):
    translations = TranslatedFields(
        image = models.ImageField(
        upload_to='slider/',
        verbose_name="Изображение",
        blank=True
        ),
    )
    created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name="Дата создания"
    )
    link = models.URLField(verbose_name='Ссылка', blank=True)
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            if img.mode in ('RGBA', "P"):
                img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG', quality=70)

            output.seek(0)

            self.image = ContentFile(output.read(), os.path.basename(self.image.name))


        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.link or 'No data'


class Feedbacks(TranslatableModel):
    translations = TranslatedFields(
        text = RichTextUploadingField(verbose_name='Отзыв', blank=True),
        author = models.CharField(max_length=200, verbose_name='Автор', blank=True)
    )
    image = models.ImageField( upload_to='feedbacks/', verbose_name='Изображение')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )


    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            if img.mode in ('RGBA', "P"):
                img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG', quality=70)

            output.seek(0)

            self.image = ContentFile(output.read(), os.path.basename(self.image.name))


        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.author or 'No data'
    

    
class Partners(models.Model):
    title = models.CharField(verbose_name='Название', blank=True, max_length=350)
    image = models.ImageField( upload_to='partners/', verbose_name='Изображение', blank=True )
    url = models.URLField(verbose_name='Ссылка', max_length=200, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
        ordering = ['-created_at']

    def __str__(self):
        return self.url



class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='videosMain/')  # Файл будет храниться в media/videos/

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def preview(self):
        if self.file:
            return mark_safe(f'''
                <video width="300" controls>
                    <source src="{self.file.url}" type="video/mp4">
                    Ваш браузер не поддерживает видео.
                </video>
            ''')
        return "(Нет видео)"

    preview.short_description = "Превью"
        
    def __str__(self):
        return self.title
    

class Info(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, verbose_name='Заголовок',blank=True, null=True),
        text = RichTextUploadingField(verbose_name='Текст',blank=True, null=True)
    )
    
    file = models.FileField(upload_to='videosMain/', verbose_name='Видеоролик')  # Файл будет храниться в media/videos/
    poster = models.ImageField(upload_to='poster/', verbose_name='Превью видео')

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'

    def preview(self):
        if self.file:
            return mark_safe(f'''
                <video width="300" controls>
                    <source src="{self.file.url}" type="video/mp4">
                    Ваш браузер не поддерживает видео.
                </video>
            ''')
        return "(Нет видео)"

    preview.short_description = "Превью"
        
    def __str__(self):
        return self.title or 'No data'