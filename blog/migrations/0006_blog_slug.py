# Generated by Django 5.2 on 2025-05-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True, verbose_name='Slug'),
        ),
    ]
