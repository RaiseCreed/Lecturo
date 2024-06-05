from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout, get_user_model

def userLogin(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        UserModel = get_user_model()

        if username=='' and password=='':
            pass
        else:
            try:
                user = UserModel.objects.get(username=username)
            except:
                context = {'error':'User does not exist!'}
            else:
                user = authenticate(request,username=username,password=password)

                if user:
                    login(request,user)
                    return redirect('home')
                else:
                    context = {'error':'Invalid credentials!'}
            
    return render(request,'login.html',context=context)


def userLogout(request):
    logout(request)

    return redirect('userLogin')
