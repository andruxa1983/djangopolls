"""polls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from question.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'question.views.question_list', name = 'Question'),
    url(r'^question_create/$', 'question.views.question_create', name = 'New'),
    url(r'^question/delete/(?P<question_id>\d+)/$', delete_question, name='delete'),
    # url(r'^question/status_new/(?P<question_id>\d+)/$', question_status_new, name='status_new'),
    # url(r'^question/status_published/(?P<question_id>\d+)/$', question_status_published, name='status_published'),
    # url(r'^question/status_decline/(?P<question_id>\d+)/$', question_status_decline, name='status_decline'),
    # url(r'^question/status_duplicate/(?P<question_id>\d+)/$', question_status_duplicate, name='status_duplicate'),
    url(r'pub/$', pub_view, name='pub_view'),
    url(r'question/(?P<question_id>\d+)/status/(?P<status_name>\S+)/change/$', change_status, name='change_status'),
    url(r'question/(?P<question_id>\d+)/$', question_detail, name='question_detail'),

]
