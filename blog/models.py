import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields

from django.utils.text import slugify


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=500, verbose_name='Заголовок', blank=True),
        text = RichTextUploadingField(verbose_name='Текст', blank=True)
    )
    
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение')
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

            if img.mode in ('RGBA', "P"):
                img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG', quality=70)

            output.seek(0)

            self.image = ContentFile(output.read(), os.path.basename(self.image.name))



        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title or 'No data'
