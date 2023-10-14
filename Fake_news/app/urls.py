from django.contrib import admin
from django.urls import path,include
from .views import FakeNews_view



urlpatterns = [
    
    path("Fake_News/",FakeNews_view.as_view(),name="news")
]
