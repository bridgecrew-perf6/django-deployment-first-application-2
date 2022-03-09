from django.shortcuts import render; 
from django.http import HttpResponse;

#Create your views here
def display(request): 
	ss = "<h2>Hello User, Welcome to Django First-Project First-App</h2>";
	return HttpResponse(ss);



