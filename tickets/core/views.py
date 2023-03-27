from django.shortcuts import render
from django.views import generic
from .models import Theme, Ticket, Question, Answer


def tests(request):
    themes = Theme.objects.all()
    data = {'themes': themes}
    return render(request, 'core/main.html', {'context': data})


def ticket(request, slug, number):
    themes = Theme.objects.all()
    tickets = Ticket.objects.filter(theme__slug=slug)
    questions = Question.objects.filter(theme__slug=slug).filter(ticket__number=number)
    answers = Answer.objects.filter(ques__ticket__number=number)
    data = {'themes': themes, 'tickets': tickets, 'questions': questions, 'answers': answers}
    return render(request, 'core/ticket.html', {'context': data})


def theme_choice(request, slug):
    themes = Theme.objects.all()
    tickets = Ticket.objects.filter(theme__slug=slug)
    data = {'themes': themes, 'tickets': tickets}
    return render(request, 'core/main.html', {'context': data})

