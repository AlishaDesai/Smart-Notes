from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view(), name='authorization'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.LogoutInterfaceView.as_view(), name='signup')
]