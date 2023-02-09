from django.shortcuts import render
from .models import Top, Bottom, Coat, Shoe, Accessory, Toptype, Bottomtype, Coattype, Shoetype, Accessorytype


# Create your views here.
def home(request):
  return render(request, 'home.html')



def closet_index(request):
    tops = Top.objects.all()
    bottoms = Bottom.objects.all()
    coats = Coat.objects.all()
    shoes = Shoe.objects.all()
    accessories = Accessory.objects.all()
    return render(request, 'closets/index.html', { 
         'tops': tops,
         'bottoms': bottoms,
         'coats': coats,
         'shoes': shoes,
         'accessories': accessories 
    })


def tops_detail(request, top_id):
    top = Top.objects.get(id=top_id)
    no_tops = Toptype.objects.exclude(id__in=top.toptypes.all().values_list('id'))
    return render(request, 'closets/tops.html', { 
        'top': top,
        'toptypes': no_tops 
    })

def bottoms_detail(request, bottom_id):
    bottom = Bottom.objects.get(id=bottom_id)
    no_bottoms = Bottomtype.objects.exclude(id__in=bottom.bottomtypes.all().values_list('id'))
    return render(request, 'closets/bottoms.html', { 
        'bottom': bottom,
        'bottomtypes': no_bottoms
    })

def coats_detail(request, coat_id):
    coat = Coat.objects.get(id=coat_id)
    no_coats = Coattype.objects.exclude(id__in=coat.coattypes.all().values_list('id'))
    return render(request, 'closets/coats.html', { 
        'coat': coat,
        'coattypes': no_coats 
    })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    no_shoes = Shoetype.objects.exclude(id__in=shoe.shoetypes.all().values_list('id'))
    return render(request, 'closets/shoes.html', {
         'shoe': shoe,
         'shoetypes': no_shoes 
    })

def accessories_detail(request, accessory_id):
    accessory = Accessory.objects.get(id=accessory_id)
    no_accessories = Accessorytype.objects.exclude(id__in=accessory.accessorytypes.all().values_list('id'))
    return render(request, 'closets/accessories.html', { 
        'accessory': accessory,
        'accessorytypes': no_accessories 
    })





#CBVs