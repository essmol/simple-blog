from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api-v1'

router = DefaultRouter()
router.register('post',views.PostListView, basename='posts')
router.register('category', views.CatetegoryViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [
#     path('po', include('allauth.urls'))
# ]
