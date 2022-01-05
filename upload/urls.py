
from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='account_app'),name='accounts'),
    path("",home,name="home"),
    path('upload_app',include('app_upload.urls',namespace="app_upload"),name="upload")
]
