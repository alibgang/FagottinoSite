from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.generic import ListView
from django.shortcuts import render_to_response

from .models import FT_Catalogue
from ftcat.models import *

#From Tutorial on filtering:
#from django.contrib.auth.models import FT_Catalogue
from .filters import FtcatFilter


# Create your views here.
#def index(request):
    #return HttpResponse("Welcome. You're at the Fagottino Site.")

def index(request):
    return render(request, 'index.html', {})

#FT Catalogue list
def ftcat_list(request):
    model = FT_Catalogue
    ftlist = FT_Catalogue.objects.all()
    return render(request, 'ftcat.html', {'ftlist':ftlist})

#FT Cat Details list
#From Tutorial:
#def instrdetails(request): #didn't work
    #instdetail_list = FT_Catalogue.objects.all()
    #instdetail_filter = InstDetailFilter(request.GET, queryset=instdetail_list)
    #return render(request, 'ftcat_details.html', {'filter': instdetail_filter})

def search(request):
    ftcat_list = FT_Catalogue.objects.all()
    ftcat_filter = FtcatFilter(request.GET, queryset=ftcat_list)
    return render(request, 'search/ftcat_details.html', {'filter': ftcat_filter})

#def InstrDetailsList(ListView):
    #model = FT_Catalogue
    #detaillist = FT_Catalogue.objects.all()
    #context_object_name = 'instrument_details'

#FT Measurments list


#Misc Catalogue list
def misccat_list(request):
    model = Misc_Catalogue
    misclist = Misc_Catalogue.objects.all()
    return render(request, 'misccat.html', {'misclist':misclist})

#Repertoire list
def rep_list(request):
    model = RepertoireList
    replist = RepertoireList.objects.all()
    return render(request, 'replist.html', {'replist':replist})

def abstract(request):
    return render(request, 'index.html', {})

def photos(request):
    return render(request, 'photos.html', {})

def glossary(request):
    return render(request, 'glossary.html', {})

def wwmeasmethods(request):
    return render(request, 'wwmeasmethods.html', {})

def repclassificationmethods(request):
    return render(request, 'repclassificationmethods.html')

def events(request):
    return render(request, 'events.html')

def citing(request):
    return render(request, 'citing.html')

def instruments(request):
    return render(request, 'index.html')

def smfggiants(request):
    return render(request, 'index.html')

#music
def music(request):
    return render(request, 'music.html')

def analysisdata(request):
    return render(request, 'analysisdata.html')

def timeline(request):
    return render(request, 'timeline.html')

def meascomp(request):
    return render(request, 'meascomp.html')

def recordings(request):
    return render(request, 'recordings.html')

def performancevideos(request):
    return render(request, 'performancevideos.html')

def endoscopicvideos(request):
    return render(request, 'endoscopicvideos.html')

def reflections(request):
    return render(request, 'reflections.html')

def publications(request):
    return render(request, 'publications.html')

def makers(request):
    return render(request, 'makers.html')

def iconography(request):
    return render(request, 'iconography.html')

def team(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'about.html')

def acknowledgements(request):
    return render(request, 'about.html')

def collectionlinks(request):
    return render(request, 'collectionlinks.html')

def librarylinks(request):
    return render(request, 'librarylinks.html')

# To use in a later version: set up classes:
#class FTListView(ListView):
    #model = FT_Catalogue
    	#added loader.get_template() andn module as listed above:
    #template_name = loader.get_template('ftcat.html')

