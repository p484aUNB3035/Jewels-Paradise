from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [

    path('home', views.home , name="Home"),
    # path('category/<int:cid>/', views.show_category, name="show_Category"),
    path('contact', views.contact, name="contact"),
    path('',views.userlogin,name="login"),
    path('handlelogout',views.handlelogout,name="handlelogout"),
    path('registration',views.registration,name="registration"),
    path('save_product_details', views.save_product_details, name='save_product_details'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
