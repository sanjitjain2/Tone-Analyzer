from django.conf.urls import url
from django.contrib import admin
from tone import views
urlpatterns = [
    url (r'^home/$',views.tone_in, name = 'home'),

    url (r'^update/$',views.tone_update, name = 'update'),

]
