from django.contrib import admin 
from rest_framework import routers
from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('menu/', views.MenuItemView.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls), name='booking'),
    path('message/', views.msg),
    path('token-auth/', obtain_auth_token)
]