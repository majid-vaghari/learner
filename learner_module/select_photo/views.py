from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from select_photo.models import LabeledNumber


def home(request):
    first = LabeledNumber.objects.filter(complete=False).first()
    next_pic = LabeledNumber.objects.filter(complete=False).exclude(id__lte=first.id).first()
    return render(request, 'select_photo/index.html', {'pic_id': first.id, 'next_id': next_pic.id})


def pic(request, pic_id):
    req_pic = get_object_or_404(LabeledNumber, id=pic_id)
    return HttpResponse(req_pic.photo.file, content_type='image/png')


def next_pic_id(request, pic_id):
    l = LabeledNumber.objects.filter(complete=False).filter(id__gt=pic_id)
    if l.count() > 0:
        return JsonResponse({'nextId': l.first().id})
    else:
        return JsonResponse({'nextId': 'null'})


def next_pic_id_c(request, pic_id):
    l = LabeledNumber.objects.filter(id__gt=pic_id)
    if l.count() > 0:
        return JsonResponse({'nextId': l.first().id})
    else:
        return JsonResponse({'nextId': 'null'})


def save_label(request, pic_id, retrieved_label):
    o = get_object_or_404(LabeledNumber, id=pic_id)
    if o.label1 is None:
        o.label1 = retrieved_label
    elif o.label2 is None:
        o.label2 = retrieved_label
    elif o.label3 is None:
        o.label3 = retrieved_label
        o.complete = True

    # o.save()

    return HttpResponseRedirect(reverse('select_photo:home'))


def show_pics(request):
    first = LabeledNumber.objects.first()
    next_pic = LabeledNumber.objects.exclude(id__lte=first.id).first()
    return render(request, 'select_photo/show.html', {'pic_id': first.id, 'next_id': next_pic.id})


def get_record(request, pic_id):
    o = get_object_or_404(LabeledNumber, id=pic_id)
    return JsonResponse({
        'id': o.id,
        'url': request.build_absolute_uri('/pic/' + str(o.id)),
        'category': o.category,
        'label1': o.label1,
        'label2': o.label2,
        'label3': o.label3,
        'completed': o.complete
    })
