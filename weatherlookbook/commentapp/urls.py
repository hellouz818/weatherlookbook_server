from django.urls import path
from . import views

urlpatterns = [
    path("comment/<int:bid>", views.commentcreate, name="coomentcreate"),
]