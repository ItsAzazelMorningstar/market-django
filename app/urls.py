#f u react
from django.urls import include, path
from .views import index
urlpatterns=[
    path("",index),
    path("sayfa1",index),
    
]