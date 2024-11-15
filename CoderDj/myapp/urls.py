from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('page2222', views.page2, name="history"),
    path('page3', views.page3, name="forum"),
    path('page4', views.page4, name="store")
]
