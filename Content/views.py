from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def show(request,book_id):
    book = Contentinfo.objects.get(id=book_id)
    return render(request,"Content/show.html",context={"book":book})

def edit(request,book_id):
    book = Contentinfo.objects.get(id=book_id)
    typeinfo = Contenttype.objects.all()
    return render(request, "Content/editor.html", context={"book": book,"typeinfo":typeinfo})

def edit_handle(request,book_id):
    try:
        book = Contentinfo.objects.get(id=book_id)
        book.title = request.POST.get("title",'')
        book.ttype_id = int(request.POST.get("type_id",''))
        book.content = request.POST.get("content","")
        book.save()
        return JsonResponse({"success":1})
    except Exception as e:
        print("=========>%s"%e)
        return JsonResponse({"success":0})

def add(request):
    return render(request,"Content/editor.html",context={})

def add_handle(request,uid):
    try:
        new_contentinfo_obj = Contentinfo()
        new_contenttype_obj = Contenttype()
        new_contentinfo_obj.title = request.POST.get("title")
        new_contentinfo_obj.author_id = uid
        new_contentinfo_obj.content = request.POST.get("content")
        type_ = request.POST.get("type").strip()
        if Contenttype.objects.filter(type=type_): # 如果已存在此分类
            type_id = Contenttype.objects.filter(type=type_)[0].id
            new_contentinfo_obj.ttype_id = type_id
            print("========>存在此分类",type_id,type_)
        else:   # 不存在
            new_contenttype_obj.type = type_
            new_contenttype_obj.save()
            print("========>已保存新分类:",type_)
            new_contentinfo_obj.ttype_id = Contenttype.objects.filter(type=type_)[0].id
        new_contentinfo_obj.save()
        return JsonResponse({"success":1})
    except Exception as e:
        print("-------------->",e)
        return JsonResponse({"success":0})

def delete(request,book_id):
    book = Contentinfo.objects.filter(id=book_id)[0]
    type_id = Contentinfo.objects.filter(id=book_id)[0].ttype_id
    book.delete()
    if Contentinfo.objects.filter(ttype_id=type_id):
        pass
    else:
        Contenttype.objects.get(id=type_id).delete()
    return JsonResponse({"success":1})