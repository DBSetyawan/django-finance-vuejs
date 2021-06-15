"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from vuedjango.views import *

# from django.urls import path
from vuedjango import views as lk
from vuedjango.views import dashboard, register
# from vuedjango.views import views as r
 

urlpatterns = [ 
    url(r'^$', index),
    url(r"^register/", register, name="register"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^admin/", admin.site.urls),
    # url(r"^", include("users.urls")),
    # url(r"^dashboard/", dashboard, name="dashboard"),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}), 
    url( r'^login/$',auth_views.LoginView.as_view(template_name="vuedjango/login.html"), name="login"),
    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="login.html"), name="logout"),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^conversation$', broadcast),
    url(r'^conversations/$', conversations),
    url(r'^conversations/(?P<id>[-\w]+)/delivered$',delivered),
    # url(r'^api/vuedjango$', lk.tutorial_list),
    # url(r'^api/vuedjango/(?P<pk>[0-9]+)$', lk.tutorial_detail),
    # url(r'^api/vuedjango/published$', lk.tutorial_list_published),
    # path('vue-test', lk.vue_test),
]
