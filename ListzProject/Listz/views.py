from django.shortcuts import render
from .models import ListItem

def home(request):
    items = ListItem.objects.all().order_by("-created_at")
    return render(request, "home.html", {"items": items})
