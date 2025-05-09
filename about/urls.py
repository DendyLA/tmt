from django.urls import path
from . import views

urlpatterns = [
	path('', views.about, name='about'),
	path('gallery/<int:pk>/', views.gallery, name='gallery')
]
