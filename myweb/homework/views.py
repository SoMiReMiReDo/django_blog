from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.views.generic import View
from django import forms
import django_excel as excel

class UploadFileForm(forms.Form):
    file = forms.FileField()

# ex:/assetinfo/test_django_excel_upload
class TestDjangoExcelUpload(View):
    """测试使用django-excel上传文件"""

    def get(self,request):
        form = UploadFileForm()
        return render(request,'upload_form.html',context={ 'form': form })

    def post(self,request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv")
        else:
            return HttpResponseBadRequest()

# ex:/assetinfo/test_django_excel_download
class TestDjangoExcelDownload(View):
    """测试使用django-excel下载文件"""

    def get(self):
        sheet = excel.pe.Sheet([[1, 2], [3, 4]])
        return excel.make_response(sheet, "xlsx")

