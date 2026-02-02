from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView 

urlpatterns = [
    path('',views.home,name="home"),
    path("api/profile/", views.profile, name="profile"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('api/register/',views.register_api,name="register_api"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]