from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate

CustomUser = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_serializer().Meta.model.objects.get(id=response.data['id'])
        token = Token.objects.get(user=user)
        response.data['token'] = token.key
        return response


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


#  Follow a user
class followuser(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)
        if target_user == request.user:
            return Response({'detail': "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
        return Response({'detail': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)


#  Unfollow a user
class unfollowuser(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)
        if target_user == request.user:
            return Response({'detail': "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target_user)
        return Response({'detail': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)