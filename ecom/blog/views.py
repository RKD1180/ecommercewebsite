from django.shortcuts import render
from .models import Blogpost,BlogheroImage
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts= Blogpost.objects.all()
    banner = BlogheroImage.objects.all().order_by('img_id')[:4]
    context = {'myposts': myposts,
           'banner':banner
    }
    return render(request, 'blog/index.html', context)

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html',{'post':post})
