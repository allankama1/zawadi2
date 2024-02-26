
from django.contrib import admin
from django.urls import path
from Hosiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('innerpage/', views.inner,name='inner'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
 ]
