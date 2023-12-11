from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect


# Search by Author and order stories from the newest to oldest
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        author_name = self.request.GET.get('author', None)
        if (author_name != None):
            return NewsStory.objects.filter(author__username=author_name).order_by('-pub_date')
        else:
            return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_name = self.request.GET.get('author', None)
        if (author_name == None):
            context['latest_stories'] = NewsStory.objects.all().order_by('-last_update')[:4]
        else:
            context['filtering'] = True
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class AddStoryView(generic.CreateView):
    form_class = StoryForm 
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm 
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')


class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteView.html'
    success_url = reverse_lazy('news:deleteSuccess')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = NewsStory.objects.get(id=self.kwargs['pk'])
        return context
    
def delete_success_view(request):
    return render(request, 'news/deleteSuccess.html')


class AddCommentView(generic.CreateView):
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")})
