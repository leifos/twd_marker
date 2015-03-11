from django.conf.urls import patterns, url
from marker import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^student/lab/(?P<lab>\d+)/$', views.student, name='student_lab_list'),

    url(r'^student/(?P<studentno>\d+)/$', views.student_form, name='student_form'),


    url(r'^student/$', views.student, name='student_list'),
    url(r'^date/(?P<year>\d{4})/(?P<month>\d{2})/$', views.date, name='date'),
    url(r'^assessment/$', views.enter_sheet, name='assessment'),

    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),


)