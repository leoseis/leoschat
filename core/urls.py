from  . import views
from django.urls import path
from  . import views

 
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout , name ='logout'),

]