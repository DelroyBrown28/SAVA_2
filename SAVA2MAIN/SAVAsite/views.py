from django.shortcuts import render
from .models import Question
from django.http import HttpResponse


def home_page(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, 'savesite_templates/home.html', context)
