#coding="utf-8"
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from .models import *
from Content.models import Contentinfo,Contenttype


def index(request):
    try:    # 如果登录
        dict_info = {}  #{分类:[Query对象]}
        if len(request.session["user_name"]):   # 如果登录成功
            user_id = request.session["user_id"]
            content_info_obj = Contentinfo.objects.filter(author_id=user_id)
            user_info_obj = Userinfo.objects.get(id=user_id)
            if len(content_info_obj) == 0:  # 无内容
                context = { "title": "首页","success": "null", "user_info_obj": user_info_obj}
                return render(request, "User/index.html", context=context)
            else:
                # 查询所有的分类
                type_list = content_info_obj.values("ttype").distinct()
                for type in type_list:
                    dict_info[Contenttype.objects.get(id=type["ttype"])] =Contentinfo.objects.filter(**type)
                context = {"success":1,"title":"首页","dict_info":dict_info,"user_info_obj":user_info_obj}
                return render(request,"User/index.html",context=context)

    except Exception as e:  # 游客访问
        print("=-====>%s"%e)
        user_id = 1
        content_info_obj = Contentinfo.objects.filter(author_id=user_id)
        user_info_obj = Userinfo.objects.get(id=user_id)
        # 查询所有的分类
        type_list = content_info_obj.values("ttype").distinct()
        for type in type_list:
            dict_info[Contenttype.objects.get(id=type["ttype"])] = Contentinfo.objects.filter(**type)
        context = {"success": 0, "title": "首页", "dict_info": dict_info, "user_info_obj": user_info_obj}
        return render(request, "User/index.html", context=context)

def register(request):
    context = {"title":"注册"}
    return render(request,"User/register.html",context)

def register_handle(request):
    try:
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        headpic = request.POST.get("headpic")
        # birth = request.POST.get("birth")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        userinfo = Userinfo()
        userinfo.username = name
        userinfo.password = pwd
        userinfo.headpic = headpic
        # userinfo.birth = birth
        userinfo.gender = gender
        userinfo.email = email
        userinfo.desc = desc
        userinfo.save()
        return redirect("user:login")  # url
    except Exception as e:
        print("=====注册处理中=====>%s"%e)
        return None

def register_exist(request,username):
    YoN = len(Userinfo.objects.filter(username=username))
    if YoN == 1:
        context={"status":1}
    else:
        context={"status":0}
    return JsonResponse(context)

def login(request):
    context = {"title":"登录"}
    return render(request,"User/login.html",context)

def loginout(request):
    request.session.flush()
    return redirect('user:index')

def login_handle(request):
    uname = request.POST.get("uname","")
    pwd = request.POST.get("pwd","")
    # remember = request.POST.get("remember", 0) # 记住密码
    users = Userinfo.objects.filter(username=uname)
    if users:
        if pwd == users[0].password:
            success = HttpResponseRedirect("/user/index") # redirect 不能保存cookies。这个可以
            # # 记住密码
            # if remember != 0:
            #     success.set_cookie("uname", uname)
            # else:
            #     success.set_cookie("uname", '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return success

        else:  # 密码错误
            context = {"title": "登录", "error_name": 0, "error_pwd": 1, 'uname': uname, 'pwd': pwd}
            return render(request, 'User/login.html', context=context)
    else:   # 用户名错误
        context = {"title": "登录", "error_name": 1, "error_pwd": 0, 'uname': uname, 'pwd': pwd}
    return render(request, 'User/login.html', context=context)

# 异步出错
# def login_handle(request):
#     try:
#         uname = request.POST.get("uname")
#         pwd = request.POST.get("pwd")
#         username = Userinfo.objects.filter(username=uname)
#         password = Userinfo.objects.filter(password=pwd)
#         if len(username) == 1:
#             if len(password) == 1: # 成功
#                 context = {"status": "success"}
#                 request.session["user_name"] = uname
#                 request.session["user_id"] = username[0].id
#             else:# 密码错误
#                 context = {"status": "pwd_error", "uname": uname, "pwd": pwd}
#         else:   # 用户名错误
#             context = {"status": "name_error", "uname": uname, "pwd": pwd}
#
#         print("=======================>%s"%json.dumps(context,ensure_ascii=False))
#         return JsonResponse(json.dumps(context,ensure_ascii=False))
#     except Exception as e:
#         print("====================>%s"%e)

# 加验证
def user_center(request):
    try:
        dict_info = {}  # {分类:[Query对象]}
        user_id = request.session["user_id"]
        content_info_obj = Contentinfo.objects.filter(author_id=user_id)
        user_info_obj = Userinfo.objects.get(id=user_id)
        type_list = content_info_obj.values("ttype").distinct()
        for type in type_list:
            dict_info[Contenttype.objects.get(id=type["ttype"])] = Contentinfo.objects.filter(**type)
        context = {"success": 1, "title": "用户中心", "dict_info": dict_info, "user_info_obj": user_info_obj}
        return render(request,"User/user_center.html",context=context)
    except Exception as e:
        print(e)
        return JsonResponse({"failed":1})

def update_info(request):
    try:
        uid = request.POST.get("uid","")
        name = request.POST.get("name","")
        gender = request.POST.get("gender","")
        email = request.POST.get("email","")
        desc = request.POST.get("desc","")
        user = Userinfo.objects.get(id=uid)
        user.username = name
        user.gender = gender
        user.email = email
        user.desc = desc
        user.save()
        return JsonResponse({"success":1})
    except Exception as e:
        return JsonResponse({"success":0})