from django.urls import path

from user.api.view import ProfileRetrieveAPIView, ProfileRetrieveUpdateAPIView

urlpatterns = [
    path('<str:username>/profile/', ProfileRetrieveAPIView.as_view()),
    path('profile/', ProfileRetrieveUpdateAPIView.as_view())
]
