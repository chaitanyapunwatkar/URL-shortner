from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Url
from .models import UrlData
import random, string
import qrcode 
# Create your views here.
def index(request):
    form = Url()
    return render(request, 'index.html',{'form': form} )

def urlShort(request):
    if request.method == "POST":
        form = Url(request.POST)
        if form.is_valid():
            short = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url = form.cleaned_data["url"]
            qrimage = qrcode.make(url)
            qrimage.save("static/image/qr.png")
            new_url = UrlData(url=url, short=short)
            new_url.save()
            short_url = "127.0.0.1:8000/"+short
            return render(request, "urls.html", {'shortened_url':short_url, 'short': short})
        
        else:
            form = Url()
        
    
def urlCreated(request):
    data = UrlData.objects.all()
    return render(request, 'urls.html', {'url':data})

def urlRedirect(request, shorts):
    data = UrlData.objects.get(short=shorts)
    
    return redirect(data.url)