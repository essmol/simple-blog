from django.contrib import admin
from django.urls import path, include


app_name = "post"

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    path("api/v1/", include("posts.api.v1.urls")),
]
