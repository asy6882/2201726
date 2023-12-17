from django.shortcuts import render, redirect
from posts.models import Post, PostImage 
from posts.forms import CommentForm, PostForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect


# Create your views here.

def feeds(request):
    user = request.user
    
    is_authenticated = user.is_authenticated
    
    print("user: ", user)
    print("is_authenticated:: ", is_authenticated)
    
    if not user.is_authenticated:
        return redirect("/users/login/")
    
    
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts":posts,
        "comment_form":comment_form,
        }
    return render(request, 'posts/feeds.html', context)

@require_POST
def comment_add(request):
    form = CommentForm(data=request.POST)
    posts = Post.objects.all()
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        
        print(comment.id)
        print(comment.content)
        print(comment.user)
        
        return HttpResponseRedirect(f"/posts/feeds/#post-{comment.post.id}")
    
    return render(request, 'posts/feeds.html', {'form': form, 'posts': posts})

        
    
    


    
    
    

def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            for image_file in request.FILES.getlist("images"):
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )
            
            url = f"/posts/feeds/#post-{post.id}"
            return HttpResponseRedirect(url)
        
    else:
        form = PostForm()   
    
    context = {"form":form}
    return render(request, "posts/post_add.html", context) 
        
    
    





