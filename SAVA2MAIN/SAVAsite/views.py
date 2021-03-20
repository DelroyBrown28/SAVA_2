from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, reverse
from .models import Question
from django.views import generic
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse


def home_page(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, 'savesite_templates/home.html', context)


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        contact = form.cleaned_data.get('contact')
        message = form.cleaned_data.get('message')

        send_mail(
            name,
            message,
            email,
            ['savirtual2021@gmail.com'],
        )
        messages.info(
            self.request, "Thanks for getting in touch, we'll get back to you ASAP!")
        return super(ContactView, self).form_valid(form)
