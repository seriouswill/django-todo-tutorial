from django.urls import path
from django.urls import path
from register import views as v
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("", views.home, name="")
    
    
    
]
