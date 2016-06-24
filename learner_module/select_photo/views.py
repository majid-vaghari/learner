import random

from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from select_photo.models import LabeledNumber


def home(request):
    first = random.choice(LabeledNumber.objects.filter(complete=False).order_by('shown')[:50])
    first.shown += 1
    first.save()
    next_pic = random.choice(LabeledNumber.objects.filter(complete=False).order_by('shown')[:50])
    return render(request, 'select_photo/index.html', {'pic_id': first.id, 'next_id': next_pic.id})


def pic(request, pic_id):
    req_pic = get_object_or_404(LabeledNumber, id=pic_id)
    return HttpResponse(req_pic.photo.file, content_type='image/png')


def next_pic_id(request, pic_id):
    prv = get_object_or_404(LabeledNumber, id=pic_id)
    prv.shown += 1
    prv.save()

    l = random.choice(LabeledNumber.objects.filter(complete=False).order_by('shown')[:50])
    return JsonResponse({'nextId': l.id})


def next_pic_id_c(request, pic_id):
    l = LabeledNumber.objects.filter(id__gt=pic_id)
    if l.count() > 0:
        return JsonResponse({'nextId': l.first().id})
    else:
        return JsonResponse({'nextId': 'null'})


def save_label(request, pic_id, retrieved_label):
    o = get_object_or_404(LabeledNumber, id=pic_id)
    try:
        setattr(o, 'label' + retrieved_label, getattr(o, 'label' + retrieved_label) + 1)
    except AttributeError:
        raise Http404

    o.save()

    return HttpResponseRedirect(reverse('select_photo:home'))


def show_pics(request):
    first = LabeledNumber.objects.first()
    try:
        first_id = first.id
    except AttributeError:
        first_id = 0
    next_pic = LabeledNumber.objects.exclude(id__lte=first_id).first()
    try:
        next_id = next_pic.id
    except AttributeError:
        next_id = 'null'
    return render(request, 'select_photo/show.html', {'pic_id': first_id, 'next_id': next_id})


def get_record(request, pic_id):
    o = get_object_or_404(LabeledNumber, id=pic_id)
    return JsonResponse({
        'id': o.id,
        'url': request.build_absolute_uri('/pic/' + str(o.id)),
        'category': o.category,
        'real_label': o.real_label,
        'label0': o.label0,
        'label1': o.label1,
        'label2': o.label2,
        'label3': o.label3,
        'label4': o.label4,
        'label5': o.label5,
        'label6': o.label6,
        'label7': o.label7,
        'label8': o.label8,
        'label9': o.label9,
        'shown': o.shown,
        'completed': o.complete
    })
