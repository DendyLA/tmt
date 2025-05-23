# Generated by Django 5.2 on 2025-04-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_services_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='Фото')),
                ('content', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
