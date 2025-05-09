
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Имя', required=True)
    last_name = forms.CharField(label='Фамилия', required=True)
    phone = forms.CharField(label='Телефон', required=False)  # уже будет в международном формате
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)