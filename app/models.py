from django.db import models

# Create your models here.

from django.db import models


class Doctor(models.Model):
    directio = (
        (1, 'Хирург'),
        (2, 'Терапевт')
    )
    direction = models.IntegerField(max_length=30, choices=directio)
    fullname = models.CharField(max_length=150)
    pincode = models.CharField(max_length=11)
    age = models.IntegerField()
    experience = models.IntegerField()
    phone = models.CharField(max_length=13)
    nurse = models.ForeignKey('Nurse', on_delete=models.PROTECT)
    patient = models.ForeignKey('Patient', on_delete=models.PROTECT)
    # image = models.ImageField()

class SiniorDoctor(models.Model):
    fullname = models.CharField(max_length=150)
    pincode = models.CharField(max_length=11)
    age = models.IntegerField()
    experience = models.IntegerField()
    phone = models.CharField(max_length=13)
    # image = models.ImageField()


class Hospital(models.Model):
    REGIONS = [
        (1, 'Chui'),
        (2, 'Naryn'),
        (3, 'Issyk-Kul'),
        (4, 'Osh'),
        (5, 'Batken'),
        (6, 'Talas'),
        (7, 'Jalal-Abad')
    ]
    OWN = [
        (1, 'Частная'),
        (2, 'Государственная')
    ]
    okpo = models.IntegerField(unique=True)
    employees = models.CharField(max_length=10)
    region = models.IntegerField(max_length=20, choices=REGIONS)
    state = models.IntegerField(max_length=20, choices=OWN)
    sinior_doctor = models.ForeignKey(SiniorDoctor, on_delete=models.PROTECT)
    # image = models.ImageField()

    def okpo_true(self, okpo):
        if okpo in (bd):
            pass #appdate bd
        else:
            print('такая уже есть')

class Nurse(models.Model):
    fullname = models.CharField(max_length=150)
    pincode = models.CharField(max_length=11)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    # image = models.ImageField()



class Patient(models.Model):
    fullname = models.CharField(max_length=150)
    pincode = models.CharField(max_length=11)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    # image = models.ImageField()



