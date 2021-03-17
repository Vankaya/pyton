from django.core.paginator import Paginator
from django.shortcuts import render
import time

from .forms import FindForm
from .models import Vacancy

def home_view(request):
    form = FindForm()

    return render(request, 'scraping/home.html', {'form': form})


def list_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    print(city, language)
    page_obj = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
        paginator = Paginator(qs,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'scraping/home.html', {'object_list': page_obj,
                                                  'form': form})

def test_rest(request):
    name = 'Ivan'
    return render(request, 'scraping/home.html', {'name': name})



