from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    """Display a list of all minerals in the database."""
    minerals = Mineral.objects.filter(name__startswith='A')
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'active': 'active'})
