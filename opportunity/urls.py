from django.urls import path
from . import views

urlpatterns = [
	path('/tenders', views.tenders, name='tenders'),
	# path('gallery/<int:pk>/', views.gallery, name='gallery')
]
