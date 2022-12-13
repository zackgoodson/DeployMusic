from django.shortcuts import render
from landing.models import Band
from django.shortcuts import redirect

# Create your views here.
def bandsPageView(request) :
        band = Band.objects.order_by('?')[:6]
        context = {
                "band" : band,
        }
        return render(request, 'bands.html', context) 


def singleBandPageView(request, bandID) :
        band = Band.objects.get(id = bandID)
        photo = Band.photo
        context = {
                "band" : band,
                "photo" : photo,
        }
        return render(request, 'viewband.html', context) 
def addbandPageView(request) :
        context ={

        }
        return render(request, 'addband.html', context)

def addband(request) :
        if request.method == "POST" :
                band = Band()
                band.bandname = request.POST['bandname']
                band.hometown = request.POST['hometown']
                band.genre = request.POST['genre']

                band.save()
                return redirect('performance')
        else :
                return render(request, 'addband.html')
