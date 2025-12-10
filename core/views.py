from django.shortcuts import render


def index(request):
    """Homepage view demonstrating Tailwind CSS integration."""
    return render(request, 'index.html')

