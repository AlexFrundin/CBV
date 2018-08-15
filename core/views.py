from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Movie, Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class MovieList(ListView):
    model = Movie
    paginate_by = 4


class MovieDetail(DetailView):
    queryset = Movie.objects.all_with_related_person()


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()






    # def movie_list(request):
    #     top = Movie.objects.all()
    #     SET_COUNT = 4
    #     paginator = Paginator(top, SET_COUNT)
    #     page = request.GET.get('page')
    #     try:
    #         top_=paginator.get_page(page)
    #     except PageNotAnInteger:
    #         top_=paginator.get_page(1)
    #     except EmptyPage:
    #         top_ = paginator.get_page(paginator.num_pages)
    #     return render(request, "name_templates", top)
