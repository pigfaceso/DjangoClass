from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    allproduct = Product.objects.all()
    context = {'pd': allproduct}
    return render(request, 'myapp/home.html', context)

def home2(request):
    return HttpResponse('<h1>Hello world2<h1>')
def aboutUs(request):
    return render(request, 'myapp/aboutus.html')

def contact(request):
    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        topic = data.get('topic')
        email = data.get('email')
        detail = data.get('detail')

        if (topic == '' or email == '' or detail == ''):
            context['message'] = 'Please, fill the all contact informations'
            return render(request, 'myapp/contact.html', context)

        newRecord = contactList()
        newRecord.topic = topic
        newRecord.email = email
        newRecord.detail = detail
        newRecord.save()

        context['message'] = 'The message has been received'
        print(topic)
        print(email)
        print(detail)
        print('-------------------')
    return render(request, 'myapp/contact.html', context)


def userlogin(request):
    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')

        try:
            user = authenticate(username=username, password=password)
            login(request, user)
        except:
            context['message'] = "username or password is incorrect"

    return render(request, 'myapp/login.html', context)


def showContact(request):
    allcontact = contactList.objects.all()
    context = { 'contact': allcontact }
    return render(request, 'myapp/showcontact.html', context)
