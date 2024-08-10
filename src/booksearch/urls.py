from django.urls import path, include
from .views.csv_view import CSVView
from rest_framework.routers import DefaultRouter

from booksearch.views.book_view import BookViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("csv/upload/", CSVView.as_view(), name="csv_view"),
]
