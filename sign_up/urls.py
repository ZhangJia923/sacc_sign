from django.conf.urls import url

from . import views

app_name = 'sign_up'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^new_actor/$',views.new_actor,name='new_actor'),
    url(r'^actors/$',views.actors,name='actors'),
    url(r'^actors/(?P<actor_id>\d+)/$',views.actor,name='actor'),
    url(r'^delete_actor/(?P<actor_id>\d+)/$',views.delete_actor,name='delete_actor'),
    url(r'^edit_actor/(?P<actor_id>\d+)/$',views.edit_actor,name='edit_actor'),
]

