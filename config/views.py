from django.shortcuts import render
from django.shortcuts import HttpResponse
def about(request):
    # return HttpResponse('Hi this website is about me')
    return render(request,'About .html')
def home(request):
    # return HttpResponse("This Page is basic page.Ha Ha Ha!")
    return render(request,'Home.html')
