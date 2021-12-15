from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.shortcuts import redirect 
from django.views import View

# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    return render(request, "myapp/index.html")

def add(request, sid):
    return HttpResponse("adding ~~ %d" % sid)

def year(request, year):
    return HttpResponse("years: %s " % year)

def nothing(request):
    raise Http404("there is nothing~~")
# 调用报错404

def resp01(request):
    return HttpResponse("相应链接")

def resp02(request):
    return redirect(reverse('resp01'))
    # return render(request, '404.html')

    # 这里是两种不同的重定向方式 

# resp03 视图类的定义！！！
class myView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello Respose View!")

def resp04(request):
    data = [
        {'id':1001, 'name':'zhangsan', 'age':20},
        {'id':1002, 'name':'lisi', 'age':22},
        {'id':1003, 'name':'wangwu', 'age':21},
    ]
    return JsonResponse({"data":data})

def resp05(request):
    # return HttpResponse("hello world!")
    return render(request, "MyNote.html")

