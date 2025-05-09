from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    image = models.ImageField(upload_to='blog', verbose_name='Изображение')
    text = RichTextUploadingField(verbose_name='Текст')
    slug = models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

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
        verbose_name = 'Блог'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
