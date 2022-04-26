from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from user.api.serializers import UserSerializers

User = get_user_model()


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    # def get(self, request, username, *args, **kwargs):
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = UserSerializers(instance=user)
    #     return Response(serializer.data)


class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializers

    def get_object(self):
        return self.request.user

# TODO: add profile list api view
# class ProfileListAPIView

# generics.RetrieveAPIView ==> get()
# generics.ListAPIView ==> get()
# generics.CreateAPIView ==> post()
# generics.UpdateAPIView ==> put()
# generics.DestroyAPIView ==> delete()
#
# generics.RetrieveUpdateAPIView ==> get() && put()
# generics.RetrieveDestroyAPIView ==> get() && delete()
# generics.RetrieveUpdateDestroyAPIView ==> get() && put() && delete()
# generics.ListCreateAPIView ==> get() && post()
