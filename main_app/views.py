from django.shortcuts import render
from .models import Closet


# Create your views here.
def home(request):
  return render(request, 'home.html')



def closet_index(request):
    closets = Closet.objects.all()
    return render(request, 'closets/index.html', { 'closets': closets })