import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from slugify import slugify

from .forms import DocumentForm
from .models import Document
from .tasks import importfile
from datetime import datetime


def demmandupload(request):
    data = {
        'title_page': "Home"
    }
    if request.method == 'POST' and request.FILES['file']:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['file']
            valid_extensions = ['.xlsx', '.xls']
            ext = os.path.splitext(myfile.name)[1]
            if ext.lower() in valid_extensions:
                now = datetime.now()
                fs = FileSystemStorage()
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                filename = fs.save(slugify(date_time+" "+myfile.name)+".xlsx", myfile)
                uploaded_file_url = fs.url(filename)
                data['uploaded_file_url'] = uploaded_file_url
                print(uploaded_file_url)
                document = Document(document=uploaded_file_url)
                document.save()
                importfile.delay(uploaded_file_url)
            else:
                data['form'] = DocumentForm()
                data['erro'] = "Arquivo não permitido"
    else:
        data['form'] = DocumentForm()

    return render(request, 'upload.html', data)
