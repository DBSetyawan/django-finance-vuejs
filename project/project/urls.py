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
from vuedjango import views as lk
from django.urls import path
 
urlpatterns = [ 
    url(r'^api/vuedjango$', lk.tutorial_list),
    url(r'^api/vuedjango/(?P<pk>[0-9]+)$', lk.tutorial_detail),
    url(r'^api/vuedjango/published$', lk.tutorial_list_published),
    path('vue-test', lk.vue_test)
]
