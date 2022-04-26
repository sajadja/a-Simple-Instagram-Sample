from django.urls import path

from activity.views import CommentListAPIView, CommentCreateAPIView

urlpatterns = [
    path('comment/', CommentListAPIView.as_view()),
    path('new-comment/', CommentCreateAPIView.as_view())
]
