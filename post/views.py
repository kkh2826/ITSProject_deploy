from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import FormView, ListView, TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from its.views import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from post.forms import PostAddForm, CommentForm
from post.models import Post, Comment
from itsapp.models import Language, Electronics
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList
from django.core.urlresolvers import reverse

class PostCreateView(LoginRequiredMixin, CreateView, FormView) :
    model = Post
    template_name = 'post/add.html'
    form_class = PostAddForm
    success_url = reverse_lazy('post:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostListView(ListView) : 
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')

        if search:
            post = Post.objects.all().filter(tag__contains=search)
        else:
            post = Post.objects.all()
        return post


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'post/tagging_post_list.html'

class C_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(lang_category__language='C언어').order_by('-create_date')

class C_Plus_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(lang_category__language='C++').order_by('-create_date')

class Python_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(lang_category__language='PYTHON').order_by('-create_date')

class Java_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(lang_category__language='JAVA').order_by('-create_date')


class HP_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(elec_category__electronics='HandPhone').order_by('-create_date')

class NB_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(elec_category__electronics='NoteBook').order_by('-create_date')

class KB_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(elec_category__electronics='KeyBoard').order_by('-create_date')

class EP_ListView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        return Post.objects.all().filter(elec_category__electronics='EarPhone').order_by('-create_date')



class CommentDetailView(DetailView):
    model = Post
    template_name = 'post/comment.html'

class CommentCreateView(CreateView, FormView) :
    model = Comment
    template_name = 'post/create_comment.html'
    form_class = CommentForm

    success_url = reverse_lazy('post:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk'))
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self, **kwargs) :
        return reverse('post:comment', kwargs={'pk': self.object.post.id })


def AddNotice(request):
    return render(request, 'post/add_notice.html')

class PostDeleteView(LoginRequiredMixin, DeleteView) :
    model = Post
    success_url = reverse_lazy('post:list')
    template_name = 'post/delete.html'


class My_ListView(ListView):
    model = Post
    template_name = 'post/mypost_list.html'

    def get_queryset(self):
        return Post.objects.all().filter(user=self.request.user).order_by('-create_date')

class Other_ListView(ListView):
    model = Post
    template_name = 'post/otherpost_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user
        return context
    
    def get_queryset(self, *args, **kwargs):
        post = super(Other_ListView, self).get_queryset(*args, **kwargs)
        return post.filter(user__username=self.kwargs['username'])
