from django.shortcuts import render
from django.http import HttpResponse

def homepage (request):
	return render(request, 'index.html')
# Create your views here.
def contactpage (request):
	return render(request, 'contact.html')
def aboutpage (request):
	return render(request, 'aboutus.html')
def newspage (request):
	return render(request, 'news.html')
def loginpage (request):
	return render(request, 'login.html')
def signuppage (request):
	return render(request, 'signup.html')
def charitypage (request):
	return render(request, 'charity.html')
def calendarpage (request):
	return render(request, 'calendar.html')
def themingpage(request):
	return render(request, 'theming.html')