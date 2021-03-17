from django.shortcuts import render


def index(request):
    """Display site home page."""
    return render(request, 'index.html')
