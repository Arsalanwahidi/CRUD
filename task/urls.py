from django.urls import path, include
from . import views

#Creating Your urls here

app_name='tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('signup/', views.sign_up, name='signup'),
]