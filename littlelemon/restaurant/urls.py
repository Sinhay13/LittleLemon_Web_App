#define URL route for index() view
from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
#from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]