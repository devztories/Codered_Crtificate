from django.shortcuts import render


def home(request):
    """Serve the public certificate generator without requiring an account."""
    return render(request, "certificates/index.html")
