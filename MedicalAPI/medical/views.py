from django.shortcuts import render
from .models import Disease
from django.http import HttpResponse



def disease_list(request):
	diseases = Disease.objects.all().order_by('date');
	#return HttpResponse(diseases)
	return render(request,'medical/disease_list.html',{'diseases':diseases})


def disease_detail(request, DrName):
	disease = Disease.objects.get(DrName=DrName)
	return render(request, 'medical/disease_detail.html', {"disease":disease})


def disease_create(request):
	return render(request, 'medical/disease_create.html')