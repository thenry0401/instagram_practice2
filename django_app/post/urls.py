from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail')
]