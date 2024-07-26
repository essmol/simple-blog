from django.shortcuts import render
from django.views.generic.base import TemplateView




class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"