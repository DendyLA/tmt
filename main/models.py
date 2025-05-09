from django.db import models
from django.utils.html import mark_safe
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify

class Subscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    def __str__(self):
        return self.email


class Slogan(models.Model):
    first_title = models.CharField(max_length=100, verbose_name="Первый Заголовок")
    second_title = models.CharField(max_length=100, verbose_name="Первый Заголовок")
    third_title = models.CharField(max_length=100, verbose_name="Первый Заголовок")

    class Meta:
        verbose_name = "Слоган"
        verbose_name_plural = "Слоганы"
    
    def __str__(self):
        return self.first_title



class Services(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news_images/', verbose_name='Фото')
    content = RichTextUploadingField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):

        if not self.slug: 
            self.slug = slugify(self.title)


        if self.image:
            img = Image.open(self.image)

            # Преобразование в RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')

            quality = 85
            output = BytesIO()
            img.save(output, format='JPEG', quality=quality, optimize=True)

            # Сжимаем до тех пор, пока не станет < 2MB или качество не опустится до 30
            while output.tell() > 2 * 1024 * 1024 and quality > 30:
                quality -= 5
                output = BytesIO()
                img.save(output, format='JPEG', quality=quality, optimize=True)

            output.seek(0)
            self.image = ContentFile(output.read(), self.image.name)
            

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Slider(models.Model):
    image = models.ImageField(
        upload_to='slider/',
        verbose_name="Изображение"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    link = models.URLField(verbose_name='Ссылка', blank=True)
    


    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            # Преобразование в RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')

            quality = 85
            output = BytesIO()
            img.save(output, format='JPEG', quality=quality, optimize=True)

            # Сжимаем до тех пор, пока не станет < 2MB или качество не опустится до 30
            while output.tell() > 2 * 1024 * 1024 and quality > 30:
                quality -= 5
                output = BytesIO()
                img.save(output, format='JPEG', quality=quality, optimize=True)

            output.seek(0)
            self.image = ContentFile(output.read(), self.image.name)

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.link


class Feedbacks(models.Model):
    image = models.ImageField( upload_to='feedbacks', verbose_name='Изображение' )
    text = RichTextUploadingField(verbose_name='Отзыв')
    author = models.CharField(max_length=200, verbose_name='Автор')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )


    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            # Преобразование в RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')

            quality = 85
            output = BytesIO()
            img.save(output, format='JPEG', quality=quality, optimize=True)

            # Сжимаем до тех пор, пока не станет < 2MB или качество не опустится до 30
            while output.tell() > 2 * 1024 * 1024 and quality > 30:
                quality -= 5
                output = BytesIO()
                img.save(output, format='JPEG', quality=quality, optimize=True)

            output.seek(0)
            self.image = ContentFile(output.read(), self.image.name)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return self.author
    

    
class Partners(models.Model):
    title = models.CharField(verbose_name='Название', blank=True, max_length=350)
    image = models.ImageField( upload_to='partners', verbose_name='Изображение' )
    url = models.URLField(verbose_name='Ссылка', max_length=200, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            # Преобразование в RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')

            quality = 85
            output = BytesIO()
            img.save(output, format='JPEG', quality=quality, optimize=True)

            # Сжимаем до тех пор, пока не станет < 2MB или качество не опустится до 30
            while output.tell() > 2 * 1024 * 1024 and quality > 30:
                quality -= 5
                output = BytesIO()
                img.save(output, format='JPEG', quality=quality, optimize=True)

            output.seek(0)
            self.image = ContentFile(output.read(), self.image.name)

        super().save(*args, **kwargs)

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
    

class Info(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = RichTextUploadingField(verbose_name='Текст')
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
        return self.title