from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Mineral


def mineral_list(request):
    """Display a list of all minerals in the database."""
    minerals = Mineral.objects.all()
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'all': 'active'})


def mineral_detail(request, pk):
    """Display the details of the selected mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    image_filename = f'minerals/images/{mineral.name}.jpg'
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'image_filename': image_filename})


def random_mineral_detail(request):
    """Display the details of a randomly selected mineral."""
    mineral = Mineral.objects.order_by('?').first()
    image_filename = f'minerals/images/{mineral.name}.jpg'
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'image_filename': image_filename})


def mineral_list_by_color(request, color):
    """
    Display a list of minerals in the database
    that belong to the selected group.
    """
    minerals = Mineral.objects.filter(color__icontains=color)
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'nav_color': color})


def mineral_list_by_group(request, group):
    """
    Display a list of minerals in the database
    that belong to the selected group.
    """
    minerals = Mineral.objects.filter(group=group)
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'nav_group': group})


def mineral_list_by_letter(request, letter):
    """
    Display a list of minerals in the database
    that begin with the selected letter.
    """
    minerals = Mineral.objects.filter(name__startswith=letter.upper())
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals, 'nav_letter': letter.upper()})


def search_minerals(request):
    term = request.GET.get('query')
    minerals = Mineral.objects.filter(
        Q(name__icontains=term)|
        Q(caption__icontains=term)|
        Q(category__icontains=term)|
        Q(group__icontains=term)|
        Q(formula__icontains=term)|
        Q(strunz_classification__icontains=term)|
        Q(crystal_system__icontains=term)|
        Q(mohs_scale_hardness__icontains=term)|
        Q(luster__icontains=term)|
        Q(color__icontains=term)|
        Q(specific_gravity__icontains=term)|
        Q(cleavage__icontains=term)|
        Q(diaphaneity__icontains=term)|
        Q(crystal_habit__icontains=term)|
        Q(streak__icontains=term)|
        Q(optical_properties__icontains=term)|
        Q(refractive_index__icontains=term)|
        Q(unit_cell__icontains=term)|
        Q(crystal_symmetry__icontains=term)
        )
    return render(request,
                  'minerals/mineral_list.html',
                  {'minerals': minerals})
