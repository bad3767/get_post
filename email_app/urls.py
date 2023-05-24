'''from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path("v",views.my_view,name='my_view'),
    path('a/', MyView.as_view(), name='my-view'),
    path('g/',GreetingView.as_view()),
    #greeting="G'day
    path("crud",crud_apiview.as_view()),
]
'''
from django.urls import path
from . import views

urlpatterns = [
	path(r'', views.crud_apiview.as_view()),
	path(r'<int:pk>/', views.crud_apiview.as_view()),
]