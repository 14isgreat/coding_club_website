from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('python/', views.python_basics, name='python'),
    path('turtle/', views.turtle, name='turtle'),
    path('html/', views.html, name='html'),
    path('css/', views.css, name='css'),
    path('django/', views.django, name='django'),
    path('pygame/', views.pygame, name='pygame'),
    path('javascript/', views.javascript, name='javascript'),
    path('java/', views.java, name='java'),
    path('about/', views.about, name='about'),  # About page view
]
