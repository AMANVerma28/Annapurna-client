from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^index/',views.index, name = "index"),
	url(r'^dashboard/',views.dash, name = "dash"),
]