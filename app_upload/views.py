from django.shortcuts import render
from django.views.generic import View
from .forms import UploadFileForm
from django.http.response import HttpResponse
import mimetypes

class UploadFile(View):
    def get(self,request):
        form = UploadFileForm()
        return render(request,"upload_file.html",{"form":form})

    def post(self,request):
        print(request.POST)
        print(request.FILES)
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.save(user=request.user,size=request.FILES["body"].size)


def download_file(request,fl_path):

    fl = open(fl_path, "r")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment"
    return response

