from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UploadFileForm
from django.http.response import HttpResponse
from .models import Flile
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
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
        return redirect("home")




def delete(request,id):
    file = Flile.objects.get(id=id).delete()
    return redirect("accounts:profile")
