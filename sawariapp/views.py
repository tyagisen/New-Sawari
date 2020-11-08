from django.shortcuts import render
from .forms import DriverForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import requests


def sign(request):
    success = False
    if request.method == 'POST':
        fm = DriverForm(request.POST)
        message1 = request.POST['name']
        message3 = request.POST['phone']
        message4 = request.POST['vehicle_type']
        message = "Name: " + message1 + "\n" + "Phone: " + message3 + "\n" + "Vehicle Type: " + message4
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ph = fm.cleaned_data['phone']
            vt = fm.cleaned_data['vehicle_type']
            driverform = Driver(name=nm, phone=ph, vehicle_type=vt)
            driverform.save()

            send_mail(
                'Driver Form',
                message,
                settings.EMAIL_HOST_USER,
                ['tyagisen@gmail.com'],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'You Are Registerd')
            success = True
            fm = DriverForm()

            def run():
                r = requests.post(
                    "http://aakashsms.com/admin/public/sms/v3/send/",
                    data={
                        'auth_token': 'e4f3525c9cf770776a4c67c97b77a3f9bdb4396fad47868c9a4f570efd255bcf',
                        'to': '9800991847',
                        'text': f'{message}'
                    })
                status_code = r.status_code
                response = r.text
                response_json = r.json()

            run()  # calling run function from models.py

    else:
        fm = DriverForm()
    return render(request, 'index.html', {'form': fm, 'success': success})
