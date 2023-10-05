from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all()[:20]
    return render(request,'posts.html', {'posts': posts })




def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    

     
 


