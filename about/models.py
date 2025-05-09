from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor_uploader.fields import RichTextUploadingField


from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название проекта')
    descr = RichTextUploadingField(verbose_name='Описание')
    image = models.ImageField(upload_to='projects__card/', verbose_name='Изображение')
    pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True, verbose_name='Презентация (PDF)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

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
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']


    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, verbose_name='Проект')
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    caption = models.CharField(max_length=255, null=True, verbose_name='Подпись к изображению alt и Slug для ссылок')

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
        verbose_name = 'Фото галереи'
        verbose_name_plural = 'Фото галереи'

    def __str__(self):
        return f"Изображение для проекта: {self.project.title}"
    


class AboutServices(models.Model):
    image = models.ImageField(upload_to='services/', verbose_name='Изображение')
    title = models.CharField(max_length=355, verbose_name='Название Услуги')
    text = RichTextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

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
        verbose_name = 'Услуга - О нас'
        verbose_name_plural = 'Услуги - О нас'

    def __str__(self):
        return f"Изображение для проекта: {self.title}"