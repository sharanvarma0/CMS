from django.shortcuts import render, get_object_or_404
from cms.models import *
from django.db.models import Q
from django.views import generic
from django.http import HttpResponse
# Create your views here.

class StoryDetail(generic.DetailView):
    model = Story
    template_name = "cms/story_detail.html" 

class StoryList(generic.ListView):
    model = Story
    context_object_name = "stories"
    template_name = "cms/story_list.html"

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    story_list = Story.objects.filter(category=category)
    heading = "Category: %s" % category.label
    return render(request, "cms/story_list.html", {
        'stories': story_list,
        'heading': heading,
        'category': category
    })

def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
        print(term)
        stories = Story.objects.filter(Q(title__contains=term) | Q(markdown_content__contains=term))
        heading = "Search Results"
        return render(request, "cms/story_list.html", {
            'stories': stories,
            'heading': heading,
       })

        
        
    
