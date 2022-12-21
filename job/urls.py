from django.urls import path, include
from .views import DeserveCandidate

urlpatterns = [
path("best_candidate/",DeserveCandidate.as_view(), name="suitable_candidate")
]