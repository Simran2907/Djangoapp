from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

def index(request):
    context={
        'variable': "this is sent"
    }
    #return HttpResponse("This is homepage")
    return render(request, 'index.html',context)

def about(request):
     return render(request, 'about.html')
    #return HttpResponse("This is about page")

def service(request):
     return render(request, 'service.html')
    #return HttpResponse("This is service page")

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")