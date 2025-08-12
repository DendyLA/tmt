from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Tenders, Vacancies


def tenders(request):
	tenders = Tenders.objects.all()

	paginator = Paginator(tenders, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	content = {
		'tenders' : page_obj
	}

	return render(request, 'opportunity/opportunity.html', content)


def vacancies(request):
	vacancies = Vacancies.objects.all()

	paginator = Paginator(vacancies, 4)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	content = {
		'vacancies' : page_obj
	}


	return render(request, 'opportunity/vacancies.html', content)



def tenders_detail(request, slug):
    tender = get_object_or_404(Tenders, slug=slug)

    return render(request, 'opportunity/tenders_detail.html', {'tender': tender})


def vacancies_detail(request, slug):
	vacancy = get_object_or_404(Vacancies, slug=slug)

	return render(request, 'opportunity/vacancies_detail.html', {'vacancy' : vacancy})