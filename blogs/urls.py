from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    path('', blogs, name="blogs"),
    path('detail/<int:id>', blog_details, name="blogs_details"),
    path('category/<str:category>', blogs, name="blogs_category"),
]