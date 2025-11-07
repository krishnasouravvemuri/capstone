from django.urls import path
from .views import detect_emotion, get_recommendation

urlpatterns = [
    path("detect/", detect_emotion, name="detect"),
    path("recommend/", get_recommendation, name="recommend"),
]
