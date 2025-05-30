from django.shortcuts import render
from .models import fraza
# Create your views here.

def index(request):
    if request.method == 'POST':
        fr = request.POST.get("fraza")
        if fr:
            fraza.objects.create(fraza=fr)
            return render(request,'index.html')
    return render(request,'index.html')