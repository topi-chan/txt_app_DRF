from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = """<html><body><p>This is the main page of the Text App.</p><br>
    It's a simple application made with RESTful API for creating and reading
    text messages.</body></html>"""
    return HttpResponse(response)
