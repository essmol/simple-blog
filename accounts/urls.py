from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
        path("", include("allauth.urls")),

    path("send-email/", views.send_email, name="send-email"),

]