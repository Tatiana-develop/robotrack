from django.contrib.auth.decorators import login_required
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^login/$', views.login_user, name='login'),
    re_path(r'^logout/$', views.logout_user, name='logout'),
    re_path(r'^register/$', views.register, name='register'),
]