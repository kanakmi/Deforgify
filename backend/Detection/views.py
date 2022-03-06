from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .util import classify_image
import platform
import os

cwd = os.getcwd()
osType = platform.system()

def Home(request):
    return render(request, 'home.html')

def resut(request):
    return render(request, 'result.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        # print(url)
        if(osType == 'Windows'):
            url = url.replace('/', '\\')
        res = classify_image(str(cwd)+url)
        # print(res)
        type = res['label']
        prob = res['probablity']
        return render(request, 'result.html', {'url': url, 'type': type, 'prob': prob})
    return render(request, 'upload.html')