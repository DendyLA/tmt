from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем данные в базе данных
            ContactMessage.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],  # сюда уже приходит номер с международным кодом
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Возвращаем успешный ответ в формате JSON для AJAX
            return JsonResponse({"status": "success", "message": "Thank you for your message!"})

        else:
            # Если форма не валидна, возвращаем ошибки
            return JsonResponse({"status": "error", "errors": form.errors})

    else:
        form = ContactForm()

    return render(request, 'contacts/contacts.html', {'form': form})
