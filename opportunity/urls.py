from django.urls import path
from . import views

urlpatterns = [
	path('tenders/', views.tenders, name='tenders'),
	path('vacancies/', views.vacancies, name='vacancies'),
	path('tenders/<slug:slug>/', views.tenders_detail, name='tender_detail'),
	path('vacancies/<slug:slug>/', views.vacancies_detail, name='vacancy_detail'),
]
