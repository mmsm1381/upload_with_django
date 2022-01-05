from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import loginform
from django.contrib.auth import authenticate , login , logout as _logout
from app_upload.models import Flile
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

form = loginform()

class Login(View):

    def get(self,request):
        return render(request,"login.html",{"form":form})

    def post(self,request):
        form = loginform(request.POST)
        if form.is_valid:
            user = authenticate(username=request.POST["username"],password=request.POST["password"])
            if not user:
                return render(request,"login.html",{"error":"username or password is not valid","form":form})
            else:
                login(request,user)
                return redirect("home")

                
def logout(request):
    _logout(request)
    return redirect("home")

@login_required
def profile(request):
    qs = Flile.objects.filter(user=request.user)
    friend_file =Flile.objects.filter(visitors__id=request.user.id)
    firend_total = friend_file.aggregate(sum('size'))
    total = qs.aggregate(Sum('size'))
    ctx = {"files":qs,"total":total["size__sum"],"friend_file":friend_file,"firend_total":firend_total["size__sum"]}
    return render(request,"profile.html",ctx)
