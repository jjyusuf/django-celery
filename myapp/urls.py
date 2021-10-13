from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CommentView

urlpatterns = [
    path('comments/', CommentView.as_view()),
]