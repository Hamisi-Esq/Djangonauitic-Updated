from django.urls import path, include
from . import views

app_name = 'accouts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]
