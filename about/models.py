import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from ckeditor.fields import RichTextField

class Project(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(max_length=255, verbose_name='Название проекта', blank=True, null=True),
		descr = RichTextUploadingField(verbose_name='Описание короткое', blank=True, null=True),
		descr_full = RichTextField(verbose_name='Описание полное', blank=True, null=True),
		pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True, verbose_name='Презентация (PDF)')
	)

	video = models.FileField(upload_to='project-videos/',  blank=True, null=True, verbose_name='видео если присутствует')
	image = models.ImageField(upload_to='projects__card/', verbose_name='Изображение')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def save(self, *args, **kwargs):
		if self.image:
			img = Image.open(self.image)

			if img.mode in ('RGBA', "P"):
				img = img.convert('RGB')

			output = BytesIO()
			img.save(output, format='JPEG', quality=70)
			output.seek(0)

			# Заменяем файл корректно
			self.image = InMemoryUploadedFile(
				output,
				'ImageField',
				f"{os.path.splitext(self.image.name)[0]}.jpg",
				'image/jpeg',
				sys.getsizeof(output),
				None
			)

		super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
		ordering = ['-created_at']


	def __str__(self):
		return self.title or "No data"

class Statistic(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(verbose_name='имя пункта', blank=True, null=True, max_length=255),
	)

	num = models.CharField(verbose_name='в цифрах', blank=True, null=True, max_length=255)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = 'Статистика'
		verbose_name_plural = 'Статистики'
		ordering = ['-created_at']


	def __str__(self):
		return self.title or "No data"


class ProjectImage(models.Model):
	project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE, verbose_name='Проект')
	image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
	caption = models.CharField(max_length=255, null=True, verbose_name='Подпись к изображению alt и Slug для ссылок')

	def save(self, *args, **kwargs):
		if self.image:
			img = Image.open(self.image)

			if img.mode in ('RGBA', "P"):
				img = img.convert('RGB')

			output = BytesIO()
			img.save(output, format='JPEG', quality=70)
			output.seek(0)

			# Заменяем файл корректно
			self.image = InMemoryUploadedFile(
				output,
				'ImageField',
				f"{os.path.splitext(self.image.name)[0]}.jpg",
				'image/jpeg',
				sys.getsizeof(output),
				None
			)

		super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'Фото галереи'
		verbose_name_plural = 'Фото галереи'

	def __str__(self):
		return f"Изображение для проекта: {self.project.title}"
    


class AboutServices(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(max_length=355, verbose_name='Название Услуги', blank=True),
		text = RichTextField(verbose_name='Описание', blank=True)
	)
	image = models.ImageField(upload_to='services/', verbose_name='Изображение')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def save(self, *args, **kwargs):
		if self.image:
			img = Image.open(self.image)

			if img.mode in ('RGBA', "P"):
				img = img.convert('RGB')

			output = BytesIO()
			img.save(output, format='JPEG', quality=70)
			output.seek(0)

			# Заменяем файл корректно
			self.image = InMemoryUploadedFile(
				output,
				'ImageField',
				f"{os.path.splitext(self.image.name)[0]}.jpg",
				'image/jpeg',
				sys.getsizeof(output),
				None
			)

		super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'Услуга - О нас'
		verbose_name_plural = 'Услуги - О нас'

	def __str__(self):
		return f"Изображение для проекта: {self.title}" or 'No data'