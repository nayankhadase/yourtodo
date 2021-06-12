from django.urls import path
from . import views


urlpatterns = [
    path('',views.Loadlogin,name='loginpage'),
    path('login',views.Login,name='login'),
    
    path('signuppage',views.Loadsignup,name='signuppage'),
    path('signup',views.Signup,name='signup'),

    path('logout',views.Userlogout,name='logout'),

    path('home',views.Home,name='home'),
    path('inserttask',views.Inserttask,name='inserttask'),
    path('delete/<int:sid>',views.Delete,name="deletetask"),
    path('edit/<int:sid>',views.Edit),
    path('update/<int:sid>',views.Update),
]