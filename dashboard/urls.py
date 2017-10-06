from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^index/',views.index, name = "index"),
	url(r'^dashboard/',views.dash, name = "dash"),
]