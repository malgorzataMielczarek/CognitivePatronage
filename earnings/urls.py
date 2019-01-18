from django.urls import path

from . import views

urlpatterns = [
	path('wyniki/', views.results, name='results'),
	path('menu/', views.main_menu, name='main_menu'),
]
