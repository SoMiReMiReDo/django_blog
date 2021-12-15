from django.urls import path, re_path

from . import views

from myapp.views import myView

# 通过路由，配置请求地址 
urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:sid>', views.add, name='madd'),
    re_path(r'^year/(?P<year>[0-9]{4})/$', views.year, name='year'),
    path("nothing", views.nothing, name='nothing'),
    
    path("resp01", views.resp01, name='resp01'),
    path("resp02", views.resp02, name='resp02'),
    path("resp03", myView.as_view(), name='resp03'),
    # 关于类的基本视图，使用的是as_view()方法

    path("resp04", views.resp04, name='resp04'),
    path("resp05", views.resp05, name='resp05'),
]
