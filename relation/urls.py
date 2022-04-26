from django.urls import path

from relation.views import FollowUnfollowCreateDestroyView, FollowersListAPIView

urlpatterns = [
    path('<str:username>/follow/', FollowUnfollowCreateDestroyView.as_view(), name='follow-unfollow'),
    path('followers/', FollowersListAPIView.as_view(), name='follow-unfollow')
]
