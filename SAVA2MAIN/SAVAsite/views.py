from django.shortcuts import render
from .models import Question
from django.http import HttpResponse


def home_page(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, 'savesite_templates/home.html', context)


def ContentManagementServiceView(request):
    context = {}
    content_management_list = ContentManagementService.Objects.all()
    context['content_management_list'] = content_management_list

    return render(request,
                  'savesite_templates/home.html',
                  context)
