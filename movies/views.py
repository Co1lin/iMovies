from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from pure_pagination.mixins import PaginationMixin
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import *

ITEMS_PER_PAGE = 16

# def index(request):
#     return render(request, 'index.html')
#
# def actors(request):
#     return render(request, 'actors.html')
#
# def comments(request):
#     return render(request, 'comments.html')

class IndexView(PaginationMixin, ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movie_list'
    paginate_by = ITEMS_PER_PAGE
    object = Movie

class ActorView(PaginationMixin, ListView):
    model = Actor
    template_name = 'actors.html'
    context_object_name = 'actor_list'
    paginate_by = ITEMS_PER_PAGE
    object = Actor

class CommentView(PaginationMixin, ListView):
    model = Comment
    template_name = 'comments.html'
    context_object_name = 'comment_list'
    paginate_by = ITEMS_PER_PAGE
    object = Comment

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie.html'

class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actor.html'

def search(request):
    search_type = 'movies'
    search_text = ''
    try:
        search_type = request.GET['search_type']
        try:
            search_text = request.GET['search_text']
        except:
            if search_type == 'movies':
                return IndexView.as_view()
            elif search_type == 'actors':
                return ActorView.as_view()
            elif search_type == 'comments':
                return CommentView.as_view()
    except:
        try:
            search_text = request.GET['search_text']
        except:
            None

    before_time = datetime.datetime.now()

    # pagination
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    if search_type == 'movies':
        movie_list = Movie.objects.filter(
                Q(name__icontains=search_text) |
                Q(introduction__icontains=search_text) |
                Q(actors__name__icontains=search_text)).distinct()
        after_time = datetime.datetime.now()
        cost_time = (after_time - before_time).microseconds
        cost_time = format(cost_time / 1000000, '.6f')

        paged = Paginator(movie_list, ITEMS_PER_PAGE, request=request)
        paged_list = paged.page(page)

        return render(request, 'index.html', {
            'total_size': Movie.objects.count(),
            'query_size': movie_list.count(),
            'movie_list': paged_list.object_list,
            'is_paginated': True,
            'page_obj': paged_list,
            'cost_time': cost_time,
            'is_search': True,
        })

    elif search_type == 'actors':
        actor_list = Actor.objects.filter(
            Q(name__icontains=search_text) |
            Q(introduction__icontains=search_text)|
            Q(movie__name__icontains=search_text)).distinct()
        after_time = datetime.datetime.now()
        cost_time = (after_time - before_time).microseconds
        cost_time = format(cost_time / 1000000, '.6f')

        paged_list = Paginator(actor_list, ITEMS_PER_PAGE, request=request).page(page)

        return render(request, 'actors.html', {
            'total_size': Actor.objects.count(),
            'query_size': actor_list.count(),
            'actor_list': paged_list.object_list,
            'is_paginated': True,
            'page_obj': paged_list,
            'cost_time':  cost_time,
            'is_search': True,
        })

    elif search_type == 'comments':
        comment_list = Comment.objects.filter(
            Q(content__icontains=search_text) |
            Q(writer__icontains=search_text) |
            Q(movie__name__icontains=search_text)).distinct()
        after_time = datetime.datetime.now()
        cost_time = (after_time - before_time).microseconds
        cost_time = format(cost_time / 1000000, '.6f')

        paged_list = Paginator(comment_list, ITEMS_PER_PAGE, request=request).page(page)

        return render(request, 'comments.html', {
            'total_size': Comment.objects.count(),
            'query_size': comment_list.count(),
            'comment_list': paged_list.object_list,
            'is_paginated': True,
            'page_obj': paged_list,
            'cost_time': cost_time,
            'is_search': True,
        })
