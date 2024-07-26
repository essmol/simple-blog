from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "post"

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    path("api/v1/", include("posts.api.v1.urls")),
    path('post/api/',views.PostListApiView.as_view(), name='post-list-api')
]
 