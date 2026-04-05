from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def students(request):
    student_api = [
        {
            "id": "1",
            "name": "sameer",
            "height": "182.7cm",
        }
    ]
    
    return HttpResponse(student_api)