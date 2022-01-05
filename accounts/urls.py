from django.urls import path
from .views import Login , logout,profile


app_name = 'accounts'

urlpatterns = [
    path('login/',Login.as_view(),name="login"),
    path('logout/',logout,name="logout"),
    path('profile/',profile,name="profile")
]
