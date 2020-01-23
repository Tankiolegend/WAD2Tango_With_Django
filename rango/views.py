from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("<a href='rango/about'>Rango </a> says hey there partner!")

def about(request):
	return HttpResponse("<a href='/'>Rango </a> says here is the about page")