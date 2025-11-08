from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
import requests

def index(request):
    return render(request, 'webapp/index.html', {"RECAPTCHA_PUBLIC_KEY": settings.RECAPTCHA_PUBLIC_KEY})


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
        email = request.POST.get('email')
        message = request.POST.get('message')
        recaptcha_response = request.POST.get('g-recaptcha-response')

        # ✅ Verify reCAPTCHA with Google
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,  # Add this in settings.py
            'response': recaptcha_response
        }
        verify = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = verify.json()

        if result.get('success'):
            # ✅ CAPTCHA passed → proceed to send email
            subject = f'New contact form submission from {email}'
            body = f"Email: {email}\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECIPIENT_EMAIL],
                fail_silently=False,
            )

            messages.success(request, "✅ Thank you! Your message has been sent successfully.")
        else:
            # ❌ CAPTCHA failed → show error
            messages.error(request, "Please confirm you’re not a robot before submitting.")

        # Redirect safely
        return redirect('/#contact')

    return render(request, "webapp/index.html")