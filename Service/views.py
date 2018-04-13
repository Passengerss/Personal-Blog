from django.shortcuts import render
from django.core.paginator import Paginator
from Content.models import Contentinfo,Contenttype

def movie_source(request,page_index):
    list_of_obj = Contentinfo.objects.all()
    a = Contentinfo.objects.filter(ttype_id__type__contains="什么")
    Paginator_obj = Paginator(list_of_obj,1)
    page_num = Paginator_obj.num_pages
    if page_index == "":
        page_index = "1"
    page_index = int(page_index)
    first_page = Paginator_obj.page(page_index)
    page_list = Paginator_obj.page_range
    data = paging(page_index,first_page,page_list,page_num)
    context = {
        "page":first_page,
        "page_list": page_list,
        "page_num":page_num,
        "left_ellipsis":data["left_ellipsis"],
        "right_ellipsis":data["right_ellipsis"],
        "left_page_index":data["left_page_index"],
        "right_page_index":data["right_page_index"],
        "first_page_show":data["first_page_show"],
        "last_page_show":data["last_page_show"],
    }
    print("==============>",a)
    return render(request,"Service/movie_source.html",context=context)
# 用来分页的函数
def paging(current_page_index,current_page,list_of_page,count_of_page):

    """
    实现分页功能：
    传入参数：
    current_page_index：当前页ID
    current_page：当前页对象
    list_of_page：一个包含所有页码的列表
    count_of_page：页码的数量
    :return:
    """
    left_ellipsis=False
    right_ellipsis=False
    left_page_index=[]
    right_page_index=[]
    first_page_show = False
    last_page_show = False
    if current_page_index == 1: # 请求第一页
        right_page_index = list_of_page[0:current_page_index+4]
        if right_page_index[-1] < count_of_page-1:    #   与最后一页之间有其他页,需要省略号
            right_ellipsis = True
        if right_page_index[-1] < count_of_page:    # 页码中不包含最后一项，需要显示最后一项
            last_page_show = True
    elif current_page_index == count_of_page:   # 访问最后一项
        left_page_index = list_of_page[(current_page_index-4) if (current_page_index-4)>0 else 0: current_page_index]
        if left_page_index[0] > list_of_page[0]+1:    # 与第一页之间存在其他页，需要省略号
            left_ellipsis = True
        if left_page_index[0] > list_of_page[0]:    # 不包含第一项，需要显示第一项
            first_page_show = True
    else:
        left_page_index = list_of_page[(current_page_index-4) if (current_page_index-4)>0 else 1: current_page_index]
        right_page_index = list_of_page[current_page_index:current_page_index+4]
        # 是否需要显示第 1 页和第 1 页后的省略号
        if left_page_index[0] > list_of_page[0]:
            first_page_show = True
        if left_page_index[0] > list_of_page[0] + 1:
            left_ellipsis = True
        # 是否需要显示最后一页和最后一页前的省略号
        if right_page_index[-1] < list_of_page[-1]:
            last_page_show = True
        if right_page_index[-1] < list_of_page[-1]-1:
            right_ellipsis = True
    data = {
        'left_ellipsis' :left_ellipsis,
        'right_ellipsis':right_ellipsis,
        'left_page_index':left_page_index,
        'right_page_index':right_page_index,
        'first_page_show' : first_page_show,
        'last_page_show' :last_page_show,
    }
    return data

def search(request,key_words):
    pass
