from django.conf.urls import url
from . import views

app_name = 'SubmitForm'

urlpatterns = [

    url(r'^$', views.SubmitForm, name='submitForm'),

    url(r'^upload_csv/$', views.upload_csv, name='upload_csv'),

]