from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homme,name='home'),
    path('<slug:slug>',views.roomchat,name='roomchat'),
    path('signup/',views.signup,name='signup'),
    path('createroom/',views.createroom,name='createroom'),
    path('deleteroom/<int:room_id>',views.deleterooom,name='deleteroom'),


    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='authentication/login.html'),name='login')
]
