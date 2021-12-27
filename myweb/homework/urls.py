from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import serve
from django.urls import re_path
from django.views import static
from django.conf.urls import url

from .views import *

app_name = 'assetinfo' # 设置命名空间

urlpatterns = [

    # ex:/assetinfo/test_django_excel_upload
    path('test_django_excel_upload', TestDjangoExcelUpload.as_view() , name='test_django_excel_upload'),

    # ex:/assetinfo/test_django_excel_download
    path('test_django_excel_download', TestDjangoExcelDownload.as_view() , name='test_django_excel_download'),
]