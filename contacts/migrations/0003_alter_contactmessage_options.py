# Generated by Django 5.2 on 2025-04-24 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contactmessage_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmessage',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
    ]
