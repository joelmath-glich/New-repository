from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Departments,Doctors
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
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctor.html',dict_docs)


def contact(request):
    return render(request,'contact.html')


def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)