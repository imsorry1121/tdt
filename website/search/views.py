from django.http import HttpResponse
from django.shortcuts import render
from website.search.models import News


# Create your views here.
def hello_world(request):
	return HttpResponse("hello world")

