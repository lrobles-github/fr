from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^friends$', views.all_friends),
    url(r'^add_friend$', views.add_friend),
    url(r'process_friend/(?P<id>\d+)$', views.process_friend),
]
