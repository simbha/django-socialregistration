from django.conf import settings
from socialregistration.compat.urls import *
from socialregistration.contrib.facebook.views import FacebookSetup, \
    FacebookRedirect, FacebookCallback
 
urlpatterns = patterns('',
    url('^redirect/$', FacebookRedirect.as_view(), name='redirect'),
    url('^callback/$', FacebookCallback.as_view(), name='callback'),
    url('^setup/$', FacebookSetup.as_view(), name='setup'),
)
