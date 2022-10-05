from django.shortcuts import render
from django.http import HttpResponse

# import Post class from models.py which is in the same directory.
from .models import Post

# using class based view , for that we need to import which type view we want.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# only logged in users can update.
from django.contrib.auth.mixins import LoginRequiredMixin

# only the current user can update their posts not others.
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.


# Let's use DB query and add them to our blog instead of our dummy data.
# Lets run a query on our post model and pass all that data.

 
def home(request):
    context ={
        'posts':Post.objects.all(),
        'title':'home'
    }
    return render(request,'blog/home.html',context)

# making a class view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # to reverse the order of the quey in the db, os that the newest post will be on the top.
    ordering =['-date_posted']



class PostDetailView(DetailView):
    model = Post
        # by defualt templates in class based view are named as,
        # <app>/<model>_<viewtype>.html
        # That is, blog/Post_Detail.html



# Create View
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']


    def form_valid(self,form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

# Update View
class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']


    def form_valid(self,form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

# This func will prevent any other user updating others posts.
    def test_func(self):
        post = self.get_object() # this is will get the post , that we are currently trying to upgrade
        # now we will check that, the current user is the author of the post.
        if self.request.user == post.author:
            # now allow them to update the post.
            return True
        else:
            return  False




# Delete View
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/home'
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else: 
            return False







def about(request):
    context ={
        'title':'About'
    }
    return render(request,'blog/about.html',context)
