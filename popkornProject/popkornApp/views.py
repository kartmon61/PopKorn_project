from django.shortcuts import render, redirect, get_object_or_404  
#from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from datetime import datetime  
from django.contrib import auth
from urllib.request import urlopen
from bs4 import BeautifulSoup 

#관리자 공지사항 Notice 추가 (사용가능)

# Create your views here.

def getDate():
        now = datetime.now() 
 
        return  '%s.%s.%s' % (now.month, now.day , now.year )

#### https://www.koreaboo.com 기준으로 데이터 가져옴 ####
def getData(url,path):
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser",from_encoding="utf-8") 
        obj =bsObject.find_all("article",{"class":"cat-news"})  
        datalist= []
        try:
                for arial in obj :
                        link = arial.select('a')[0].get('href')
                        title = arial.select('a')[0].get('aria-label') 
                        src = arial.select('source')[0].get('data-srcset').split(" ")[0]
                        data = {}
                        data["link"] = link
                        data["title"] = title
                        data["src"] = src    
                        datalist.append(data)
        except:
                redirect(path)
        return datalist

def index(request):
    datalist = getData("https://www.koreaboo.com/news/","index") 
    return render(request,'index.html',{'data':datalist})

 
def news(request):  
    datalist = getData("https://www.koreaboo.com/news/","news")
    return render(request,'news.html',{'data':datalist,'now':getDate()}) 

def media(request):
        return render(request,'media.html')

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


def calendar(request):
    return render(request,'calendar.html')


 

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
                        except IntegrityError as e:
                             auth.logout(request)    
                             return redirectForm(request,'username is already exist')   
                        except:
                            auth.logout(request)
                            return redirectForm(request,'error!')   
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


 