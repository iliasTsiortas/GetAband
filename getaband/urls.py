from django.urls import re_path

from . import views

app_name = 'GetAband'

urlpatterns = [
    re_path('^users/?$', views.UserList.as_view()),
    re_path(r'^users/(?P<pk>\d+?$)', views.Userprofile.as_view()),
]