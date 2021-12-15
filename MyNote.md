### 前言

最近正好想要搭建一个个人博客，正巧期末python的大作业就是用python的Django框架的搭建一个网站，所以就利用这次机会学习一下Django然后搭一个自己的博客。~~如果能狗一个服务器就更好了呢~~



### 学习资料

>1. 学习视频	www.bilibili.com/video/BV1iU4y1A7MH
>2. Django框架配置    https://blog.csdn.net/qq_42274565/article/details/102644399
>3. Django说明文档    https://docs.djangoproject.com/en/4.0/

moli	xiaoche06

### Django命令行应用

1. 安装Django第三方库 pip install django
2. 创建一个Django项目 django-admin startproject XXX (项目名)
3. 用管理器(manger.py) 
   1. 创建应用 py manage.py startapp myBlog(应用名)
   2. 启动项目 py manage.py runserver XXX(端口) **本地访问**
   2. 启动项目 py manage.py runserver 0.0.0.0:8000 **远程访问**
   2. 数据迁移 py manage.py migrate (需要配置好数据库)
   2. 创建超级用户 py manage.py createsuperuser 




### 创建用户中心

1. 项目配置文件setting.py

   1. ```python
      LANGUAGE_CODE = 'zh-hans' # 配置网站语言为中文
      ```

   2. ```python
      TIME_ZONE = 'Asia\Beijing' # 配置网站时间为北京
      ```

2. 配置静态文件以及用户上传文件的相关设置

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',	# 用来管理静态文件
   ]
   ```

3. 激活虚拟环境

   ![image-20211208181932534](https://github.com/SoMiReMiReDo/_picgo/find/main/image-20211208181932534.png)
   
   需要有以下虚拟环境，可以参见命令行3.1 进行创建
   
   

### **首先要创建模型数据**

   > 模型数据是一个类，需要在users文件夹下的models.py 中定义，直接与数据库进行交互。

   在创建模型数据之前，我们**首先把应用注册到setting.py文件中**

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',   # todo 用来管理静态文件
       'myBolg.apps.MyBolgConfig'      # todo bolg应用
       'users.apps.UsersConfig'        # todo users应用（定义的用户中心）
   ]
   ```

   通过 xxx.apps.XxxConfig 的方式实现注册

   #### 配置User模型

可以直接导入 from django.contrib.auth.models import User

这里提供的是最基本的用户模型，如果想要拥有其他的个人信息则需要扩展个人模型

#### 关联关系扩展用户

~~~python
class UserProfile(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')	# 一个用户对应唯一一组数据
~~~

Django提供了三种数据库的关联方式，一对一、多对一、多对多

~~~python
OneToOneField	ForeignKey	ManyToManyField
~~~

添加用户信息：

~~~python
nike_name = modes.CharField('ID', max_length=12, blank=True, default='')
~~~

向用户的不同的信息申请不同的字段：

例如在这里需要用户的ID，就申请了CharField字符字段，类似的还有DateField日期字段等等，可以参考基本数据类型

#### URL配置

- 要从URL捕获一个值，需要使用尖括号括起来。

- 捕获的值可以选择转换器类型。**<int:name> 捕获整型参数，并命名为name。**

  ~~~python
  path("find/<int:sid>", view.find, name='find')
  ~~~

  

- 无需添加/

> 常用的路径转换器如下：
>
> - '/'str	匹配任何非空字符串，但是路径分隔符除外'/'。
> - int    匹配零或任何正整数。
> - slug   匹配由ASCII字母或数字以及字符和下划线组成的任何条形字符串。
> - uuid  匹配格式化的UUID。
> - path  匹配任何非空字符串，包括路径分隔符'/'。

**使用正则表达式：**

1. 如果路径和转换器语法不足以定义URL模式，则可以使用正则表达式。即，使用re_path()代替path()。
2. 在python正则表达式中，命名正则表达式组的语法为(?P<name>patten),其中name是组的名称，并且patten是匹配的某种形式。

~~~python
re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive)
~~~

PS：正则返回的参数是字符串类型。



#### 404界面设置

~~~html
 <!DOCTYPE html>
<html>
<head>
    <title>404</title>
</head>
<body>
    <center>
    <h2>404 hot found</h2>
    <h3>{ {  exception  } } </h3>
    </center>
</body>
</html>
~~~

默认模板如下

#### 在一个View的方法中调用其他方法

~~~python
from django.urls import reverse

print(reverse("add"))

~~~

通过路由名称反向生成url请求地址，执行重定向

可以用其构建出来url路由地址访问其他网页



### Django视图框架

cookie设置：

~~~python
def resp_cookie(request):
	# 设置响应对象
    response = HttpResponse('cookie的设置')
    
    # 使用响应对象进行cookie的设置
    response.set_cookie('key','value')
    
    # 这里可以用重定向，导入首页
    return response
~~~









