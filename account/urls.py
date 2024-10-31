from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('profile/retrieve/', RetrieveProfileView.as_view()),
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/update/<int:id>/', UpdateProfileView.as_view()),
    path('profile/delete/<int:id>/', DeleteProfileAPIView.as_view()),
    path('workers/create/', WorkerCreateAPIView.as_view()),
    path('reset_password/', PasswordResetView.as_view()),

]