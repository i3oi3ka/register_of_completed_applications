from django.contrib.auth import views as auth_views
from django.urls import path

from .views import UserDetail, UserCreate, UserList, UserUpdate, password_reset_request
from .views import login_view, logout_view

urlpatterns = [
    path('user_list/', UserList.as_view(), name='users_list'),
    path('user-detail/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('auth/sign-up/', UserCreate.as_view(), name='user_create'),
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/p_r_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/r_token.html'),
         name='password_reset_confirm'),
    path('reset/done',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/r_done.html'),
         name='password_reset_complete'),

]
