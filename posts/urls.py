from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    path('posts', include('posts.api.v1.urls'))
]
