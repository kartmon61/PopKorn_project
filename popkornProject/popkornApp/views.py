from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting,PostingComent,Notice
#관리자 공지사항 Notice 추가 (사용가능)

# Create your views here.
def header(request):
    return render(request,'header.html')

def index(request):
    return render(request,'index.html')

def footer(request):
    return render(request,'footer.html')

def news(request):
    return render(request,'news.html')

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
    return render(request,'community.html',{'posts':posts})

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
#     coments = one_post.postcoment_set.all()
    return render(request,'communityshow.html',{'posts':one_post})

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

def comentcreate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.postcoment_set.create(content=request.POST['coment_content'])
    return redirect('/community/show/'+str(post_id))

def comentdelete(request,post_id):

    one_coment = get_object_or_404(PostingComent,id=coment_id,post=post_id)
    one_coment.delete()
    return redirect('/community/show/'+str(post_id))


#---------------------community--------------------------------#