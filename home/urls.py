from django.urls import path, include
from .import views
from .views import predict
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctor/',views.doctor,name='doctor'),
    path('contact/',views.contact,name='contact'),
    
    path('department/',views.department,name='department'),
      path('predict/', predict, name='predict'),
]
