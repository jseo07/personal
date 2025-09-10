from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme


def index(request):
    return render(request, 'webapp/index.html')


def sp(request):
    return render(request, 'webapp/projects/sp.html')

def smartmove(request):
    return render(request, 'webapp/projects/smartmove.html')

def gan(request):
    return render(request, 'webapp/projects/gan.html')

def llm(request):
    return render(request, 'webapp/projects/llm.html')

def lstm(request):
    return render(request, 'webapp/projects/lstm.html')

def knn(request):
    return render(request, 'webapp/projects/knn.html')

def tetris(request):
    return render(request, 'webapp/projects/tetris.html')

def housing(request):
    return render(request, 'webapp/projects/housing.html')

def contact(request):
    if request.method == 'POST':
        email   = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'New contact form submission from {email}'
        body = (
            f"Email: {email}\n"
            f"Message:\n{message}"
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECIPIENT_EMAIL],
            fail_silently=False,
        )

        messages.success(request, "Thank you, message has been sent.")
        next_url = request.POST.get('next', '/')
        if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
            next_url = '/'
        return redirect(next_url)
    return render(request, "webapp/index.html")