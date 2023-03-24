from django.urls import path
from . import views


urlpatterns = [
    path('', views.tests, name='tests'),
    path('<str:slug>/<int:number>', views.ticket, name='ticket'),
    path('<str:slug>/', views.ticket_choice, name='ticket_choice')
]
