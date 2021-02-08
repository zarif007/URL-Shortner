import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Url


def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        prefix = request.POST['prefix']

        uid = prefix
        if prefix == '':
            uid = str(uuid.uuid4())[:5]
        
        find = Url.objects.filter(uuid=uid).count()
        if find: 
            return HttpResponse('invalid')
        else:
            try:
                new_url = Url(link=link, uuid=uid)
                new_url.save()
                return HttpResponse(uid)
            except:
                return HttpResponse('invalid')
 
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)