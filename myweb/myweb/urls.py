"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import serve
from django.urls import re_path
from django.views import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('article/', include('article.urls')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('comment/', include('comment.urls', namespace='comment')),

    # 第三方库
    # path('password-reset/', include('password_reset.urls')),
    # re_path('^stiaic/(?P<path>.*)',serve,{'document_root':settings.STATIC_ROOT}),
    # re_path('^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),     

    # url(r'^static/(?P<path>.*)$', static.serve,
    #   {'document_root': settings.STATIC_ROOT}, name='static'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
