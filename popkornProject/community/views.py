from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Posting,PostingComment,Notice 
from django.contrib.auth.models import User
from .forms import CommunityCreate


# Create your views here.
def community(request):
    posts = Posting.objects.all()
    paginator = Paginator(posts,10) 
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)

    return render(request,'community.html',{'page_posts':page_posts})

def communitynew(request):
        if request.method == 'POST':
                form = CommunityCreate(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('')
                else:
                        return redirect('index')
        else:
                form = CommunityCreate()
                return render(request, 'communitynew.html', {'form': form})
 
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

def communityedit(request, post_id):
    if request.method == "POST":
        #수정 저장
        one_post = Posting.objects.get(pk = post_id)
        form = CommunityCreate(request.POST, instance=one_post)
        if form.is_valid():
             form.save()
             return redirect('/community/show/'+str(one_post.id))
    else:
        #수정 입력
        one_post = Posting.objects.get(pk = post_id)
        if one_post.author == User.objects.get(username = request.user.get_username()):
                one_post = Posting.objects.get(pk = post_id)
                form = CommunityCreate(instance = one_post)
                return render(request, 'communityedit.html', {'posts' : one_post, 'form' : form})
        else:
                return redirectForm(request, 'Not allow edit this post!') 

def communityupdate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.title = request.POST['title']
        one_post.content = request.POST['content']
        one_post.save()

        return redirect('/community/show/'+str(one_post.id))

# def communitydelete(request,post_id):
#     one_post = get_object_or_404(Posting,id=post_id)
#     one_post.delete()
#     return redirect('/community')


def communitydelete(request, post_id):
    one_post = Posting.objects.get(pk = post_id)
    if one_post.author == User.objects.get(username = request.user.get_username()):
        one_post.delete()
        return redirect('/community')
    else:
        return redirectForm(request, 'Not allow delete this post!' )

##########################comment #######################################

def commentcreate(request,post_id):
    if(request.method == 'POST'):
        one_post = get_object_or_404(Posting,id=post_id)
        one_post.postingcomment_set.create(content=request.POST['comment_content'],author=request.POST['comm_nm'])
    return redirect('/community/show/'+str(post_id))

def commentdelete(request,post_id,comment_id):
        one_comment = get_object_or_404(PostingComment,id=comment_id,posting=post_id)
        if one_comment.author == User.objects.get(username = request.user.get_username()):
                one_comment = get_object_or_404(PostingComment,id=comment_id,posting=post_id)
                one_comment.delete()
                return redirect('/community/show/'+str(post_id))
        else:
                return redirectForm(request, 'Not allow delete this comment!' )


def redirectForm(request,msg):
        return render(request, 'redirect.html', {'msg': msg})



