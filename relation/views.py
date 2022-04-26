from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from relation.models import Relation
from relation.serializers import FollowersSerializers

User = get_user_model()


class FollowUnfollowCreateDestroyView(View):

    def get_object(self):

        try:
            user = User.objects.get(username=self.kwargs.get('username'))
        except User.DoesNotExists:
            raise Http404
        return user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        qs = Relation.objects.filter(from_user=request.user, to_user=user)
        if qs.exists():
            qs.delete()
            cache.decr('{}:followers'.format(user.username))
            cache.get_or_set('{}:followings'.format(request.user.username), request.user.followings.count())
            cache.decr('{}:followings'.format(request.user.username))
        else:
            Relation.objects.create(from_user=request.user, to_user=user)
            cache.incr('{}:followers'.format(user.username))
            cache.get_or_set('{}:followings'.format(request.user.username), request.user.followings.count())
            cache.incr('{}:followings'.format(request.user.username))
        return redirect('/{}/'.format(user.username))


class FollowersListAPIView(generics.ListAPIView):
    queryset = Relation.objects.select_related('from_user').all()
    serializer_class = FollowersSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(to_user=self.request.user)
