from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Departments,Doctors
from .forms import BookingForm
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
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    else:
        form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)


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

# filepath: c:\Users\joelm\OneDrive\Desktop\Django project\tutorial\home\views.py
import pickle
from django.shortcuts import render
from django.http import JsonResponse
import numpy as np

def predict(request):
    if request.method == 'POST':
        data = request.POST
        features = [float(data['feature1']), float(data['feature2']), float(data['feature3']), float(data['feature4'])]

        # Load model
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Make prediction
        prediction = model.predict([features])[0]

        return JsonResponse({'prediction': prediction})

    return render(request, 'predict.html')