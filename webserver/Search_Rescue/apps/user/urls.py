from django.conf.urls import url, include

from rest_framework import routers

from .views import UserListView, UserTestListView

app_name = '[user]'

urlpatterns = [
    url(r'^user/list/$', UserListView.as_view()),
    url(r'^user/test/$', UserTestListView.as_view()),
]
