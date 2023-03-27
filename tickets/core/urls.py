from django.urls import path
from . import views


urlpatterns = [
    path('<str:slug>/<int:number>/', views.ticket, name='ticket'),
    path('<str:slug>/', views.theme_choice, name='theme_choice'),
    path('', views.tests, name='tests'),
]
