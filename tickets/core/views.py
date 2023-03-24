from django.shortcuts import render
from django.views import generic
from .models import Theme, Ticket, Question, Answer


def tests(request):
    themes = Theme.objects.all()
    data = {'themes': themes}
    return render(request, 'core/main.html', {'context': data})


def ticket(request, slug, number):
    themes = Theme.objects.all()
    questions = Question.objects.filter(theme__slug=slug).filter(ticket__number=number)
    answers = Answer.objects.filter(ques__ticket__number=number)
    data = {'themes': themes, 'questions': questions, 'answers': answers}
    return render(request, 'core/ticket.html', {'context': data})

def ticket_choice(request, slug):
    themes = Theme.objects.all()
    data = {'themes': themes}
    return render(request, 'core/main.html', {'context': data})

