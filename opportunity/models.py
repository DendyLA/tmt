from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from parler.models import TranslatableModel, TranslatedFields

from django.utils.text import slugify

class Tenders(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(verbose_name='Заголовок', max_length=255, blank=True, null=True),
		text = RichTextUploadingField(verbose_name='Текст', blank=True, null=True),
	)
	slug = models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)

	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

	class Meta:
		verbose_name = "Тендер"
		verbose_name_plural = "Тендеры"
		ordering = ['-created_at']

	def __str__(self):
		return self.title or 'Nothing'
	
	# def save(self, *args, **kwargs):
	# 	if not self.slug and self.title:
	# 		self.slug = slugify(self.title)
	# 	super().save(*args, **kwargs)



