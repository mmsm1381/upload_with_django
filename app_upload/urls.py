from django.urls import path
from .views import UploadFile , download_file


app_name = 'app_upload'

urlpatterns = [
    path('uploadfile/',UploadFile.as_view(),name="uploadfile"),
    path('download<str:fl_path>/',download_file,name="download")
]
