from django.urls import path
from .views import UploadFile , delete


app_name = 'app_upload'

urlpatterns = [
    path('uploadfile/',UploadFile.as_view(),name="uploadfile"),
    path('delete<int:id>/',delete,name="delete")
]
