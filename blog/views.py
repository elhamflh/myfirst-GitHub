from cgitb import html
from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import datetime
from .models import Article, Authur

def home (request):
    
    context = {
        "articles": [
            {
                "title" : "MICK JAGGER", 
                "img": "https://artlogic-res.cloudinary.com/w_2000,h_2000,c_limit,f_auto,fl_lossy,q_auto:low/artlogicstorage/maddoxgallery/images/view/9a7d87e244f6e796a8a223d3e810b051j.jpg",
                "des" : "1971 Edition of 250 plus 50 artist's proofs Screen print on Arches Aquarelle (rough) Paper 110.5 x 74 cm"
                },
            {
                "title" : "MICK JAGGER", 
                "img": "https://artlogic-res.cloudinary.com/w_2000,h_2000,c_limit,f_auto,fl_lossy,q_auto:low/artlogicstorage/maddoxgallery/images/view/9a7d87e244f6e796a8a223d3e810b051j.jpg",
                "des" : "1971 Edition of 250 plus 50 artist's proofs Screen print on Arches Aquarelle (rough) Paper 110.5 x 74 cm"
                },
            {
                "title" : "MICK JAGGER", 
                "img": "https://artlogic-res.cloudinary.com/w_2000,h_2000,c_limit,f_auto,fl_lossy,q_auto:low/artlogicstorage/maddoxgallery/images/view/9a7d87e244f6e796a8a223d3e810b051j.jpg",
                "des" : "1971 Edition of 250 plus 50 artist's proofs Screen print on Arches Aquarelle (rough) Paper 110.5 x 74 cm"
                }
                ]
                }
    return render (request, "blog/home.html", context)

def mainposts(request):
    html= Article.objects.all()
    context={"context":html}
    return render(request,"templates\blog\home.html",context)


    

# Create your views here.

def single_post(request,pk):
    html=Article.objects.get(pk=pk)
    context={"context" :html}
    return render (request,"single_post.html",context)
    
 