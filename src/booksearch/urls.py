from django.urls import path
from .views.csv_view import CSVView

urlpatterns = [
    path("csv/upload/", CSVView.as_view(), name="csv_view"),
]
