from django.urls import path
from .views import *

app_name = "portfolio"

urlpatterns = [
    path('', portfolioes, name="portfolios"),
    path('detail/<int:id>', portfolio_detail, name="portfolio_detail"),
]