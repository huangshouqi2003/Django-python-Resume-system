from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import mail
from django.contrib import messages
from hsq_account_management.forms import MuneForm,RegisterForm
from hsq_account_management.models import userinfo
import json
# Create your views here.
def index(request):
    if request.method=="GET":
        return render(request,"main_mune.html")
    else:
        muneform=MuneForm(request.POST)
        if muneform.is_valid():
            data_list = userinfo.objects.all()
            for obj in data_list:
                if (obj.account == request.POST.get("email")
                        and obj.password==request.POST.get("password")):
                    return HttpResponse("登录成功")
            return HttpResponse("邮箱或密码有错，忘记密码请联系管理员")
        else:
            if "email" in muneform.errors.get_json_data():
                messages.error(request, muneform.errors.get_json_data()['email'][0]['message'])
            if "password" in muneform.errors.get_json_data():
                messages.error(request, muneform.errors.get_json_data()['password'][0]['message'])
            return render(request,"main_mune.html")
def register(request):
    if request.method=="GET":
        return HttpResponse("不可访问")
    else:
        return  render(request,"main_register.html")
def send_mail_code(request):
    if(request.method=="GET"):
        return HttpResponse("不可访问")
    else:
        registerform = RegisterForm(request.POST)
        if "email" in registerform.errors.get_json_data():
            messages.error(request, registerform.errors.get_json_data()['email'][0]['message'])
            return render(request, "main_register.html")
        mail.send_mail(
            subject='验证码',  # 题目
            message='1111',  # 消息内容
            from_email='2245059994@qq.com',  # 发送者[当前配置邮箱]
            recipient_list=[request.POST.get('email')],  # 接收者邮件列表
        )
        messages.error(request,"已经发送，请注意查收")
        return render(request,"main_register.html")
def register_succeed(request):
    if request.method=="GET":
        return HttpResponse("不可访问")
    else:
        flag=0
        registerform = RegisterForm(request.POST)
        if "email" in registerform.errors.get_json_data():
            messages.error(request, registerform.errors.get_json_data()['email'][0]['message'])
            flag = 1
        if "password" in registerform.errors.get_json_data():
            messages.error(request, registerform.errors.get_json_data()['password'][0]['message'])
            flag=1
        if "repassword" in registerform.errors.get_json_data():
            messages.error(request, registerform.errors.get_json_data()['repassword'][0]['message'])
            flag=1
        if "mail_code" in registerform.errors.get_json_data():
            messages.error(request, registerform.errors.get_json_data()['mail_code'][0]['message'])
            flag=1
        if flag==0:
            data_list=userinfo.objects.all()
            for obj in data_list:
                if(obj.account==request.POST.get("email")):
                    return HttpResponse("邮箱有重复，忘记找管理员")
            userinfo.objects.create(account=request.POST.get("email"),password=request.POST.get("password"))
            messages.error(request,"注册成功")
        return  render(request,"main_register.html")

