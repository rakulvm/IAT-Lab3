from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    path('about/', views.about, name='about'),  # URL pattern for the about page
    path(r'myapp/', include('myapp.urls1')),
]