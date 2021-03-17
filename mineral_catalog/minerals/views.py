from django.shortcuts import get_object_or_404, render

from .models import Mineral


def mineral_list(request):
    """Display a list of all minerals in the database."""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Display the details of the selected mineral."""
    mineral = get_object_or_404(Mineral, pk=pk)
    image_filename = 'minerals/images/{}.jpg'.format(mineral.name)
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'image_filename': image_filename})


def random_mineral_detail(request):
    """Display the details of a randomly selected mineral."""
    mineral = Mineral.objects.order_by('?').first()
    image_filename = 'minerals/images/{}.jpg'.format(mineral.name)
    return render(request,
                  'minerals/random_mineral_detail.html',
                  {'mineral': mineral,
                   'image_filename': image_filename})
