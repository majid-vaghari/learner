from django.conf.urls import url

from select_photo import views

app_name = 'select_photo'

urlpatterns = [
    url(r'^$', view=views.home, name='home'),
    url(r'^pic/(?P<pic_id>[1-9][0-9]*)$', view=views.pic),
    url(r'^next/(?P<pic_id>[1-9][0-9]*)$', view=views.next_pic_id),
    url(r'^next/c/(?P<pic_id>[1-9][0-9]*)$', view=views.next_pic_id_c),
    url(r'^save/(?P<pic_id>[1-9][0-9]*)/(?P<retrieved_label>[0-9])$', view=views.save_label),
    url(r'^result/$', view=views.show_pics),
    url(r'^get/(?P<pic_id>[1-9][0-9]*)$', view=views.get_record)
]
