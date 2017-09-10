from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hellos(request, number):
    text = "<h1>Welcome to my app number %s!</h1>" % number
    return HttpResponse(text)

def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today" : today})
