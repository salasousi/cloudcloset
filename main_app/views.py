from django.shortcuts import render
from .models import Top, Bottom, Coat, Shoe, Accessory


# Create your views here.
def home(request):
  return render(request, 'home.html')



def closet_index(request):
    tops = Top.objects.all()
    bottoms = Bottom.objects.all()
    coats = Coat.objects.all()
    shoes = Shoe.objects.all()
    accessories = Accessory.objects.all()
    return render(request, 'closets/index.html', 
        { 'tops': tops,
         'bottoms': bottoms,
         'coats': coats,
         'shoes': shoes,
         'accessories': accessories },
    )