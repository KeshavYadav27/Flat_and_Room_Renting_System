from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('owner_page', views.owner_page, name='owner_page'),
    path('add_property', views.add_property, name='add_property'),
    path('owner_profile', views.owner_profile, name='owner_profile'),
    path('owner_chat_customer', views.owner_chat_customer, name='owner_chat_customer'),
    path('customer_page', views.customer_page, name='customer_page'),
    path('customer_profile', views.customer_profile, name='customer_profile'),
    path('customer_search_property', views.customer_search_property, name='customer_search_property'),
    path('customer_chat_owner', views.customer_chat_owner, name='customer_chat_owner'),
]
