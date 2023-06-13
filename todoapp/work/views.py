from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

from .models import Work

from datetime import datetime, timedelta

from .utils import get_plot

# Create your views here.


def create_date_range(count):
    to_day = datetime.now()

    _slovar = {}

    for x in range(count):
        new_date = to_day - timedelta(days=x + 1)
        new_date = str(new_date.strftime("%Y-%m-%d"))
        count_works = Work.objects.filter(date__contains=f'{new_date}').count()

        _slovar[new_date] = count_works

    _slovar = dict(sorted(_slovar.items(), key=lambda item: item[1]))
    return _slovar

def create_paginate(request):




    # list_works = Work.objects.filter(date__contains=f'{to_day}')

    # list_works = Work.objects.filter(date__contains=f'{to_day}')
    # list_works = Work.objects.filter(price__gte='25000')
    # list_works = Work.objects.filter(price__gt='25000')
    list_works = Work.objects.all().order_by('-date')

    paginator = Paginator(list_works, 15)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
        # page_obj = paginator.get_page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)


    return page_obj

def create_graph():
    pass

    # qs = Sale.objects.all()
    # x = [x.item for x in qs]
    # y = [x.price for x in qs]
    #
    # chart = get_plot(x, y)

def list_works(request):

    page_obj = create_paginate(request)

    _slovar = create_date_range(7)

    chart = get_plot(_slovar)

    context = {
        # 'list_works': list_works,
        'page_obj': page_obj,
        'chart': chart
    }

    return render(request, 'works/index.html', context)

