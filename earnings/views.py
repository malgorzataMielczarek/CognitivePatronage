from django.shortcuts import render

from .models import Earnings

def results(request):
	r_list=Earnings.objects.all()
	context={'results_list': r_list}
	return render(request, 'results.html', context)
	
	
def main_menu(request):
	return render(request, 'main_menu.html')
	
	
