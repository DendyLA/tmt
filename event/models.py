from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields
from django.conf import settings
import os

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from django.utils.text import slugify
from django.utils.formats import date_format

class Event(TranslatableModel):

	tranlate = TranslatedFields( 
		title = models.CharField(max_length=250, verbose_name="Заголовок", blank=True),
		text = RichTextUploadingField(verbose_name='О Мероприятии', blank=True),
		city = models.CharField(verbose_name='Город проведения', max_length=200, blank=True),
	)

	event_date = models.DateField(verbose_name='Дата начало',blank=True)
	event_end_date = models.DateField(verbose_name='Дата окончания',blank=True)

	image = models.ImageField(upload_to='event_images/', verbose_name='Фото', blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True, max_length=250, verbose_name='Slug', blank=True)	

	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'

	def __str__(self):
		return self.title or 'No data'
	
	
	def save(self, *args, **kwargs):
		if self.image:
			# Открытие изображения
			img = Image.open(self.image)

			# Преобразование в RGB (на случай PNG и др.)
			if img.mode in ("RGBA", "P"):
				img = img.convert("RGB")

			# Сжатие изображения
			output = BytesIO()
			img.save(output, format='JPEG', quality=70)  # quality: от 1 до 95
			output.seek(0)

			# Сохранение в поле image
			self.image = ContentFile(output.read(), os.path.basename(self.image.name))


		if not self.slug and self.title:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('event_detail', kwargs={'slug': self.slug})
	

	def get_event_period(self):
		"""Форматированный вывод диапазона дат с i18n"""
		if self.event_date and self.event_end_date:
			# Если в одном месяце и году
			if (self.event_date.month == self.event_end_date.month 
				and self.event_date.year == self.event_end_date.year):
				return f"{self.event_date.day} – {self.event_end_date.day} {date_format(self.event_date, 'F Y')}"
			
			# Если разные месяцы, но один год
			if self.event_date.year == self.event_end_date.year:
				return f"{date_format(self.event_date, 'd F')} – {date_format(self.event_end_date, 'd F Y')}"
			
			# Если разные годы
			return f"{date_format(self.event_date, 'd F Y')} – {date_format(self.event_end_date, 'd F Y')}"
		
		elif self.event_date:  # Только начало
			return date_format(self.event_date, "d F Y")
		return ""
	


class EventAbout(TranslatableModel):
	translate = TranslatedFields(
		text = RichTextUploadingField(verbose_name='текст', blank=True)
	)

	image = models.ImageField(upload_to='event__about', verbose_name='Фото', blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'О Мероприятии'
		verbose_name_plural = 'О Мероприятии'


	def save(self, *args, **kwargs):

		if self.image:
			img = Image.open(self.image)

			if img.mode in ('RGBA', "P"):
				img = img.convert('RGB')

			output = BytesIO()
			img.save(output, format='JPEG', quality=70)

			output.seek(0)

			self.image = ContentFile(output.read(), os.path.basename(self.image.name))

		return super().save(*args, **kwargs)


class EventDirection(TranslatableModel):
	translate = TranslatedFields(
		name = models.CharField(verbose_name='Название', max_length=225, blank=True)
	)

	image = models.ImageField(upload_to='event__directions', blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Направления'
		verbose_name = 'Направлении'

	def save(self, *args, **kwargs):
		if self.image:
			img = Image.open(self.image)

			if img.mode in ('RGBA', 'P'):
				img = img.convert('RGB')

			output = BytesIO()
			img.save(output, format='JPEG', quality=70)

			output.seek(0)

			self.image = ContentFile(output.read(), os.path.basename(self.image.name))

		return super().save(*args, **kwargs)
	

class EventPackb2b(TranslatableModel):
	translate = TranslatedFields(
		name = models.CharField(verbose_name='Название', max_length=225, blank=True)
	)

	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'b2b'
		verbose_name = 'b2b'


class EventPackb2g(TranslatableModel):
	translate = TranslatedFields(
		name = models.CharField(verbose_name='Название', max_length=225, blank=True)
	)

	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'b2g'
		verbose_name = 'b2g'

		

class Programme(TranslatableModel):
	translate = TranslatedFields(
		file = models.FileField( upload_to='programme/')
	)

	class Meta:
		verbose_name = 'Programme'
		verbose_name = 'Programme'


class Catalog(TranslatableModel):
	translate = TranslatedFields(
		file = models.FileField( upload_to='catalog/')
	)

	class Meta:
		verbose_name = 'Catalog'
		verbose_name = 'Catalog'