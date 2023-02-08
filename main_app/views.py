from django.shortcuts import render


# Create your views here.
def home(request):
  return render(request, 'home.html')

class Closet:  
  def __init__(self, category):
    self.category= category

  

closets = [
  Closet('TOPS'),
  Closet('BOTTOMS'),
  Closet('SHOES')
]


def closet_index(request):
  return render(request, 'closets/index.html', { 'closets': closets })