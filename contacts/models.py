from django.db import models

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона', null=True)  
    email = models.EmailField(verbose_name='Емейл')
    message = models.TextField(verbose_name='Текст')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"