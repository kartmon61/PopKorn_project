from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.core.paginator import Paginator
from .models import Mediaboard,Mcategory
from django.contrib.auth.models import User
from popkornApp.views import redirectForm
from bs4 import BeautifulSoup 

# Create your views here.

def board_create(request,board):
        #youtube embed src html parsing
        try :
                bs = BeautifulSoup(request.POST['m_content'], 'html.parser')
                obj = bs.iframe 
                board.title = request.POST['m_title'] 
                board.murl = obj['src']
                if request.POST['category_'] != "":
                        board.category = request.POST['category_']
                else:
                        board.category = request.POST['category']

                board.save() 
        except :  
                return redirectForm(request,'unverified url')
        

def media(request):
        board = Mediaboard.objects.all().order_by('-id')
        category = Mcategory.objects.all()
        keyword = request.GET.get('search')
        if keyword is not None:
                board = get_list_or_404(Mediaboard,category=keyword)
        
        paginator = Paginator(board,5) 
        page = request.GET.get('page')
        page_posts = paginator.get_page(page)

        return render(request,'media.html',{'page_posts':page_posts,'category':category})

def create(request):
        print("------------push-------------")
        if request.method =='POST':
                board = Mediaboard()
                board_create(request,board)
        return redirect('/mediaboard')

def delete(req,board_id):
    board = get_object_or_404(Mediaboard,id=board_id)
    board.delete()
    return redirect('/mediaboard')

def edit(req,board_id): 
     category = Mcategory.objects.all()
     edit_board = get_object_or_404(Mediaboard,id=board_id)
     return render(req,'media.html',{'board':edit_board,'category':category})

def update(request,board_id):
    if(request.method=='POST'):
        board = get_object_or_404(Mediaboard,id=board_id)
        board_create(request,board)
    return redirect('/mediaboard')
