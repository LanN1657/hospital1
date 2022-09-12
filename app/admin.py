from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SiniorDoctor, Hospital, Doctor, Nurse, Patient

admin.site.register(Hospital)
admin.site.register(SiniorDoctor)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
