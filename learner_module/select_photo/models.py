from django.db import models


class LabeledNumber(models.Model):
    photo = models.ImageField(upload_to='./db/photos/')
    category = models.CharField(max_length=20)
    real_label = models.IntegerField()
    label0 = models.IntegerField(default=0)
    label1 = models.IntegerField(default=0)
    label2 = models.IntegerField(default=0)
    label3 = models.IntegerField(default=0)
    label4 = models.IntegerField(default=0)
    label5 = models.IntegerField(default=0)
    label6 = models.IntegerField(default=0)
    label7 = models.IntegerField(default=0)
    label8 = models.IntegerField(default=0)
    label9 = models.IntegerField(default=0)
    shown = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
