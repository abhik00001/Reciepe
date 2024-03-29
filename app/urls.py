from django.urls import path
from app import views

urlpatterns = [
    path('', views.home , name="home"),
    path('login', views.login_page , name="login"),
    path('signup', views.signup_page , name="signup"),

    path('savedata', views.savedata),
    path('delete/<int:id>', views.deletethis),
    path('update/<int:id>', views.updatethis),
    path('updatedata/<int:up_id>', views.updatedata),
    path("search" , views.search),
   
    path('add_data', views.add_data),
]
