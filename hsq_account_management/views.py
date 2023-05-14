from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import mail
from django.contrib import messages
from hsq_account_management.forms import MuneForm
import json
# Create your views here.
def index(request):
    if request.method=="GET":
        return render(request,"main_mune.html")
    else:
        userkk=MuneForm(request.POST)
        if userkk.is_valid():
            return  HttpResponse("登录成功")
        else:
            if "email" in userkk.errors.get_json_data():
                messages.error(request, userkk.errors.get_json_data()['email'][0]['message'])
            if "password" in userkk.errors.get_json_data():
                messages.error(request, userkk.errors.get_json_data()['password'][0]['message'])
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
        mail.send_mail(
            subject='验证码',  # 题目
            message='1111',  # 消息内容
            from_email='2245059994@qq.com',  # 发送者[当前配置邮箱]
            recipient_list=[request.POST.get('mail')],  # 接收者邮件列表
        )
        messages.error(request,"已经发送，请注意查收")
        return render(request,"main_register.html")

