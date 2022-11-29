from django.shortcuts import render
from django.http import JsonResponse

def blog_list(request):
    data = {
        "message": "This is the love of my life",
    }
    return JsonResponse(data)
