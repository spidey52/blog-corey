from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Post

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  ## userpassestextin by the corey to validate user
from django.contrib.auth.models import User
# Create your views here.

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context )

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    # ordering = ['-date_posted'] ## i have already defined in model.py
    paginate_by =  5

   

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'

    # ordering = ['-date_posted'] ## i have already defined in model.py
    paginate_by =  5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)

        

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    context_object_name = 'postEdit'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'your post is created')
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    context_object_name = 'post'
    fields = ['title', 'content']

    # def form_valid(self, form):
    #     if form.instance.author == self.request.user:
    #         messages.info(self.request, 'your post is updated')
    #         return super().form_valid(form)
    #     else:
    #         messages.warning(self.request, 'you are not the author of this blog')
    #         return redirect('blog-home')

    ### another way of doing user validation by corey is
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.info(self.request, 'your post is updated')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def sat(request):
    return render(request, 'blog/sat.html', context={'hello': 'world'})



