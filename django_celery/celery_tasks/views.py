from django.shortcuts import render
from django.core.cache import cache


def task2(request):
    template = "pages/task2.html"
    # context = cache.get('statistic_covid')
    return render(request, template)

