from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time
from .tasks import sendEmail
import requests


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")
