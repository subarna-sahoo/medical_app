from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
	#return HttpResponse("This is the HomePage of >> CORE_view")
	return render(request,'homepage.html')


def nextpage(request):
	#return HttpResponse("next >> home page")
	return render(request,'nextpage.html')