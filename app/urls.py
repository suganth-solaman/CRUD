from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="home" ),
    path('register', views.register, name="register"),
    path('login_pro', views.login_pro, name="login_pro"),
    path('signout', views.signout, name="signout"),
    path('edit/<str:pk>', views.edit, name="edit"),
    path('delete/<str:pk>', views.delete, name="delete"),

]
