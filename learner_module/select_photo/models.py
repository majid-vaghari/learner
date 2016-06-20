from django.db import models


class LabeledNumber(models.Model):
    photo = models.ImageField(upload_to='./db/photos/')
    category = models.CharField(max_length=20)
    label1 = models.CharField(default=None, blank=True, null=True, max_length=1)
    label2 = models.CharField(default=None, blank=True, null=True, max_length=1)
    label3 = models.CharField(default=None, blank=True, null=True, max_length=1)
    complete = models.BooleanField()
