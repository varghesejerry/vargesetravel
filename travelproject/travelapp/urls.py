from . import views
from django.urls import path

urlpatterns = [
   #path('', views.demo, name='demo')
   # path('', views.about, name='about'),
   # path('add/', views.addition, name='addition')
    path('', views.index, name='index')
]
