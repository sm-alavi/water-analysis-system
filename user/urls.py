from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userLoad, name='user'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-delete/<str:pk>', views.userDelete, name='user-delete'),
    path('user-update/<str:pk>', views.userUpdate, name='user-update'),
    
    path('activity/', views.userActivity, name='activity'),

    path('profile/', views.profileUpdate, name='profile'),
]
