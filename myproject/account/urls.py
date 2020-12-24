from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns=[
    path('',views.home, name='home'),
    re_path(r'^signup/$',views.signup,name='signup'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]