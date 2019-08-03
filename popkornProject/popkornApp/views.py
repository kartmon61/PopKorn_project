from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting,PostingComment,Notice
from django.contrib.auth.models import User
#from django.utils import timezone
from datetime import datetime 
from django.core.paginator import Paginator
from django.contrib import auth
from urllib.request import urlopen
from bs4 import BeautifulSoup

#관리자 공지사항 Notice 추가 (사용가능)

# Create your views here.

def getDate():
        now = datetime.now() 
 
        return  '%s.%s.%s' % (now.month, now.day , now.year )

def index(request):
    return render(request,'index.html')

 
def news(request): 
    html = urlopen("https://www.koreaboo.com/news/")  
    bsObject = BeautifulSoup(html, "html.parser",from_encoding="utf-8") 
    obj =bsObject.find_all("article",{"class":"cat-news"})  
    datalist= []
    for i,arial in enumerate(obj) :
        link = arial.select('a')[0].get('href')
        title = arial.select('a')[0].get('aria-label') 
        src = arial.select('source')[0].get('data-srcset').split(" ")[0]
        data = {}
        data["link"] = link
        data["title"] = title
        data["src"] = src   
        datalist.append(data)
    return render(request,'news.html',{'data':datalist,'now':getDate()}) 

#-----------------chart iframe htmls-----------
def chart(request):
    return render(request,'chart.html') 

def chartmelon(request):
    return render(request,'melon.html')

def chartgini(request):
    return render(request,'gini.html')

def chartbuks(request):
    return render(request,'buks.html')

def chartmnet(request):
    return render(request,'mnet.html')    
#----------------------------------------------
def media(request):
    return render(request,'media.html')

def calendar(request):
    return render(request,'calendar.html')


#---------------------community--------------------------------#

def community(request):
    posts = Posting.objects.all()
    paginator = Paginator(posts,10) 
    page = request.GET.get('page') 
    page_posts = paginator.get_page(page)

    return render(request,'community.html',{'posts':posts,'page_posts':page_posts})

def communitynew(request):
    return render(request,'communitynew.html')

def communitycreate(request):
    new_post = Posting()
    new_post.title = request.POST['title']
    new_post.content = request.POST['content']
    new_post.save()
    return redirect('/community')

def communityshow(request,post_id):
    one_post = get_object_or_404(Posting,id=post_id)
    comments = one_post.postingcomment_set.all()

    return render(request,'communityshow.html',{'posts':one_post,'comment':comments})

def communityedit(request,post_id):
    one_post = get_object_or_404(Posting,id=post_id)

    return render(request,'communityedit.html',{'posts':one_post})

def communityupdate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.title = request.POST['title']
        one_post.content = request.POST['content']
        one_post.save()

        return redirect('/community/show/'+str(one_post.id))

def communitydelete(request,post_id):
    one_post = get_object_or_404(Posting,id=post_id)
    one_post.delete()
    return redirect('/community')

def commentcreate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.postingcomment_set.create(content=request.POST['comment_content'])
    return redirect('/community/show/'+str(post_id))

def commentdelete(request,post_id,comment_id):

    one_comment = get_object_or_404(PostingComment,id=comment_id,posting=post_id)
    one_comment.delete()
    return redirect('/community/show/'+str(post_id))


#---------------------community--------------------------------#


#---------------------------login------------------------------#

def signup(request):
        if request.method == 'POST':
                if request.POST['sign_pw1'] == request.POST['sign_pw2']: 
                        try:
                                user = User.objects.create_user(
                                        username=request.POST['sign_id'],
                                        password=request.POST['sign_pw1'])   
                                auth.login(request,user) 
                                print('signup has been completed !')
                        except :
                               return redirectForm(request, 'username is already exist')   
                        return redirect('index')
                else : 
                        return redirectForm(request, 'passwords must be matched!') 
            

 
def login(request):
        if request.method == 'POST':
                username = request.POST['login_id']
                password = request.POST['login_pw'] 
                user = auth.authenticate(request, username=username, password=password) 

                if user is not None:
                        auth.login(request,user)  
                        return redirect('index')
                else: 
                        return redirectForm(request, 'username or password is incorrect.') 
        else:
                return render(request, 'index.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')

 
 ############  폼 처리 후 리다이렉션 #######################
def redirectForm(request,msg):
        return render(request, 'redirect.html', {'msg': msg}) 


 