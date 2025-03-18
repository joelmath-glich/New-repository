from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # person={
    #     'name':'john',
    #     'age':30,
    #     'place':'calicut',
    # # }
    numbers={
        'num':30,
    }
    return render(request,'index.html',numbers)


def about(request):
    return render(request,'about.html')


def booking(request):
    return render(request,'booking.html')


def doctor(request):
    return render(request,'doctor.html')


def contact(request):
    return render(request,'contact.html')


def department(request):
    return render(request,'department.html')