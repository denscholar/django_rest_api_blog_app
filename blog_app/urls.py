from django.urls import path
from .views import *

urlpatterns = [
    path('blog_list/', blog_list, name="blog_list")
]
