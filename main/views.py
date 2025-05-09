from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .forms import SubscribeForm

from .models import Slider, Slogan, Services, News, Feedbacks, Partners, Video, Info

def main(request):
    slides = Slider.objects.all().order_by('created_at')
    slogans = Slogan.objects.all()
    services = Services.objects.all()
    latest_news = News.objects.order_by('-pub_date')[:3]
    feedbacks = Feedbacks.objects.all()
    partners = Partners.objects.order_by('created_at')
    video = Video.objects.last()
    infoVideo = Info.objects.last()
    return render(request, 'main/main.html', {'slides' : slides, 'slogans': slogans, 'services' : services, 'latest_news': latest_news, 'feedbacks' : feedbacks, 'partners' : partners, 'video': video, 'infoVideo' : infoVideo})


@require_POST  # Разрешаем только POST-запросы
def subscribe(request):
    # Для AJAX-запросов
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 'Thank You'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    
    # Для обычных форм (без JavaScript)
    form = SubscribeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Thank You')
    else:
        messages.error(request, 'Please write correct email')
    return redirect('home')




def news_list(request):
    all_news = News.objects.order_by('-pub_date')
    paginator = Paginator(all_news, 9)  # 9 новостей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news_list.html', {'page_obj': page_obj})


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    latest_news = News.objects.order_by('-pub_date')[:3]
    return render(request, 'main/news_detail.html', {'news': news, 'latest_news' : latest_news})

