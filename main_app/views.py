from django.shortcuts import render, redirect
import uuid
import boto3
from .models import Top, Bottom, Coat, Shoe, Accessory, Topphoto, Bottomphoto, Coatphoto, Shoephoto, Accessoryphoto


S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'cloudcloset2023'


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
    return render(request, 'closets/tops.html', { 'top': top})

def bottoms_detail(request, bottom_id):
    bottom = Bottom.objects.get(id=bottom_id)
    return render(request, 'closets/bottoms.html', { 'bottom': bottom })

def coats_detail(request, coat_id):
    coat = Coat.objects.get(id=coat_id)
    return render(request, 'closets/coats.html', { 'coat': coat })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'closets/shoes.html', { 'shoe': shoe })

def accessories_detail(request, accessory_id):
    accessory = Accessory.objects.get(id=accessory_id)
    #no_accessories = Accessorytype.objects.exclude(id__in=accessory.accessorytypes.all().values_list('id'))
    return render(request, 'closets/accessories.html', { 
        'accessory': accessory,
       # 'accessorytypes': no_accessories 
    })


def add_top_photo(request, top_id):
    top_photo_file = request.FILES.get('top-photo-file', None)
    if top_photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + top_photo_file.name[top_photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(top_photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            topphoto = Topphoto(url=url, top_id=top_id)
            topphoto.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('t_detail', top_id=top_id)


def add_bottom_photo(request, bottom_id):
    bottom_photo_file = request.FILES.get('bottom-photo-file', None)
    if bottom_photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + bottom_photo_file.name[bottom_photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(bottom_photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            bottomphoto = Bottomphoto(url=url, bottom_id=bottom_id)
            bottomphoto.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('b_detail', bottom_id=bottom_id)


def add_coat_photo(request, coat_id):
    coat_photo_file = request.FILES.get('coat-photo-file', None)
    if coat_photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + coat_photo_file.name[coat_photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(coat_photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            coatphoto = Coatphoto(url=url, coat_id=coat_id)
            coatphoto.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('c_detail', coat_id=coat_id)


def add_shoe_photo(request, shoe_id):
    shoe_photo_file = request.FILES.get('shoe-photo-file', None)
    if shoe_photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + shoe_photo_file.name[shoe_photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(shoe_photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            shoephoto = Shoephoto(url=url, shoe_id=shoe_id)
            shoephoto.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('s_detail', shoe_id=shoe_id)


def add_accessory_photo(request, accessory_id):
    accessory_photo_file = request.FILES.get('accessory-photo-file', None)
    if accessory_photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + accessory_photo_file.name[accessory_photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(accessory_photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            accessoryphoto = Accessoryphoto(url=url, accessory_id=accessory_id)
            accessoryphoto.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('a_detail', accessory_id=accessory_id)


#CBVs