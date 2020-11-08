from django.db import models
from .validators import validate_number
from django.core import validators
import requests



class Driver(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True, validators=[validate_number])
    vehicle_type = models.CharField(max_length=100)

    def run(self, *args, **kwargs):
        r = requests.post(
            "http://aakashsms.com/admin/public/sms/v3/send/",
            data={
                'auth_token': '1271c391761e586555c3c0339d7403a22c6cf55e7fa0da30fc40aa0a506224e7',
                'to': '9800991847',
                'text': f"Name:{self.name} \n Phone: {self.phone} \n vehicle Type: {self.vehicle_type}"
            })
        status_code = r.status_code
        response = r.text
        response_json = r.json()
emp1 = Driver()
