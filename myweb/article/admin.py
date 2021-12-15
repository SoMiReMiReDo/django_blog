from django.contrib import admin
from article.models import ArticlePost

# Register your models here.

# 如果要将自定义的应用程序添加到后台，则需要在这里导入

admin.site.register(ArticlePost)
