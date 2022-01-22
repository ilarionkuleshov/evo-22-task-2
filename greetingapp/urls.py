from django.urls import path
from . import views


urlpatterns = [
	path('', views.greeting, name='greeting'),
	path('visitors-list/', views.visitors_list)
]
