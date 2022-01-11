from django.urls import path
from .views import HumanView, DogView, welcome

urlpatterns = [
    path('', welcome),
    path('humans', HumanView.as_view()),
    path('dogs',DogView.as_view())
]