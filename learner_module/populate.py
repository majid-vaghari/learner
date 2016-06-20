from os import listdir
from os.path import isfile, join, basename

from django.core.files import File

from select_photo.models import LabeledNumber

only_files = [f for f in listdir('remaining samples') if isfile(join('remaining samples', f))]

for f in only_files:
    django_file = File(open('remaining samples/' + f))
    ln = LabeledNumber()
    ln.photo.save(f, django_file)
    ln.category = 'remaining samples'
    ln.save()
