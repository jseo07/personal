from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sp", views.sp, name="sp"),
    path("smartmove", views.smartmove, name="smartmove"),
    path("gan", views.gan, name="gan"),
    path("lstm", views.lstm, name="lstm"),
    path("llm", views.llm, name="llm"),
    path("knn", views.knn, name="knn"),
    path("tetris", views.tetris, name="tetris"),
    path("contact", views.contact, name="contact"),
]
