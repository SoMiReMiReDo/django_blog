from django.core import paginator
from django.shortcuts import render, resolve_url
from django.http import HttpResponse, Http404
import markdown
from django.shortcuts import render, redirect
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import ArticlePost
from django.db.models import Q
from comment.models import Comment
 
# moli id is 5.
def article_list(request):
    search = request.GET.get('search')
    if search:
        article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        search = ''
        article_list = ArticlePost.objects.all()

    paginator = Paginator(article_list, 9)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles, 'search': search }
    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    
    # 取出文章评论
    comments = Comment.objects.filter(article=id)

    context = { 'article': article, 'comments': comments }
    return render(request, 'article/detail.html', context)

def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            # new_article.author = User.objects.get(id=1)
            new_article.author = User.objects.get(id=request.user.id)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)

def article_delete(request, id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article_list")

def article_safe_delete(request, id):
    # if request.method == 'POST':
    article = ArticlePost.objects.get(id=id)
    if article.author == request.user.id:
        article.delete()
        return redirect("article_list")
    else:
        return HttpResponse("没有删除权限")
    # else:
        # return HttpResponse("仅允许post请求")

# 更新文章
def article_update(request, id):
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    if article.author != request.user.id:
        return HttpResponse("没有修改权限")
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)


