from django.shortcuts import render, redirect, get_object_or_404
from board.models import Board
from board.forms import BoardAddForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, FormView, DetailView
from its.views import LoginRequiredMixin
from hitcount.views import HitCountDetailView
from django.core.urlresolvers import reverse_lazy


class BoardListView(ListView):
    model = Board
    template_name = 'board/index.html'

    def get_queryset(self):
        search = self.request.GET.get('search2')
        type = self.request.GET.get('type')

        if search and type:
            if type == 'title':
                list = Board.objects.all().filter(title__contains=search)
            elif type == 'content':
                list = Board.objects.all().filter(content__contains=search)
            elif type == 'user':
                list = Board.objects.all().filter(user__username=search)
        else:
            list = Board.objects.all()
        return list.order_by('-id')



class BoardCreateView(LoginRequiredMixin, CreateView, FormView) :
    model = Board
    template_name = 'board/add.html'
    form_class = BoardAddForm
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BoardCreateView, self).form_valid(form)
    
    
class BoardUpdateView(LoginRequiredMixin, UpdateView) :
    model = Board
    template_name = 'board/add.html'
    form_class = BoardAddForm
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BoardUpdateView, self).form_valid(form)

class BoardDeleteView(LoginRequiredMixin, DeleteView) :
    model = Board
    success_url = reverse_lazy('board:index')
    template_name = 'board/delete.html'

class BoardDetailView(HitCountDetailView):
    model = Board
    template_name = 'board/view.html'
    count_hit = True



