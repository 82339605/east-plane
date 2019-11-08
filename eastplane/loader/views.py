import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    get = getIn.objects.all()
    leave = left.objects.all()
    use = ''
    if 'uid' in request.session and 'username' in request.session:
        use = user.objects.get(id = request.session['uid'])
    return render(request,'plane.html',locals())
def register(request):
    if request.method == 'GET':
        if 'uid' in request.session and 'username' in request.session:
            return redirect('/')
        return render(request,'register.html')
    else:
        logname = request.POST.get('login','null')
        username = request.POST.get('username','null')
        pwd = request.POST.get('password','null')
        reg = user()
        reg.log_name = logname
        reg.username = username
        reg.pwd = pwd
        reg.save()
        request.session['username'] = username
        request.session['uid'] = reg.id
        return redirect('/')
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        loginname = request.POST['login']
        pwd = request.POST['password']
        use = user.objects.filter(log_name=loginname,pwd = pwd)
        if use:
            request.session['username'] = use[0].username
            request.session['uid'] = use[0].id
            return redirect('/')
        return render(request,'login.html',locals())
def logout(request):
    if 'uid' in request.session and 'username' in request.session:
        del request.session['uid']
        del request.session['username']
    return redirect('/')
def check(request):
    lname = request.GET['lname']
    statu = 1
    msg = '合法用户名'
    if user.objects.filter(log_name=lname):
        statu = 0
        msg = '此用户已存在'
    resp = {
        'status':statu,
        'msg':msg
    }
    resp = json.dumps(resp)
    return HttpResponse(resp)
def shopping(request):
    t = ticket.objects.all()
    return render(request,'shop.html',locals())

