from django.shortcuts import render,redirect

# Create your views here.


def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name=='hp' and pwd=='123':
            return redirect('/index/')
            # return render(request,'index.html',{'name':name})

    return render(request,'login.html')

def index(request):
    return render(request,'index.html')