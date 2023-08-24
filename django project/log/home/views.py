from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

def index(request):
    return render(request,'index.html')
    # return HttpResponse('This is homepage.')

def about(request):
    return render(request,'about.html')
    #return HttpResponse('This is about page.')

def service(request):
    return render(request,'service.html')
    #return HttpResponse('Service Page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name, email=email, phone=phone, date=datetime.today())
        contact.save()

    return render(request,'contact.html')