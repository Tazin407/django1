from django.http import HttpResponse

def contact(response):
    return HttpResponse("This is the gitted contact page")

def home(response):
    return HttpResponse("This is the home of git")
