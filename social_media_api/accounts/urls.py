from django.urls import path
from .views import RegisterView, LoginView, ProfileView, followuser, unfollowuser

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', followuser.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', unfollowuser.as_view(), name='unfollow-user'),
]
