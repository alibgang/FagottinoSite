from django.urls import path

from .import views
from ftcat import views
from ftcat.views import ftcat_list
#from ftcat.search import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('ftcat', views.ftcat, name='ftcat'),
    path('ftcat_list/', views.ftcat_list, name='ftcat_list'),
    path('misccat_list/', views.misccat_list, name='misccat_list'),
    path('rep_list/', views.rep_list, name='rep_list'), 

    # instrument details URL
    path('search/', views.search, name='search'),

#next try:
    #path(r'^searchdetails/', FilterView.as_view(filterset_class=InstrDetailFilter,
        #template_name='searchdetails/ftcat_details.html'), name='searchdetails'),

    

    # instrument measurements URL
    #path('searchmeasurements/', views.search, name='searchmeasurements'),

    #photo gallery
    path('photos/', views.photos, name='photos'),
    # individual page URLs
    path('abstract/', views.abstract, name='abstract'),
    path('glossary/', views.glossary, name='glossary'),
    path('wwmeasmethods/', views.wwmeasmethods, name='wwmeasmethods'),
    path('repclassificationmethods/', views.repclassificationmethods, name='repclassificationmethods'),
    path('events/', views.events, name='events'),
    path('citing/', views.citing, name='citing'),
    path('instruments/', views.instruments, name='instruments'),
    path('smfggiants/', views.smfggiants, name='smfggiants'),
    path('music/', views.music, name='music'),
    path('analysisdata/', views.analysisdata, name='analysisdata'),
    path('timeline/', views.timeline, name='timeline'),
    path('meascomp/', views.meascomp, name='meascomp'),
    path('recordings/', views.recordings, name='recordings'),
    path('performancevideos/', views.performancevideos, name='performancevideos'),
    path('endoscopicvideos/', views.endoscopicvideos, name='endoscopicvideos'),
    path('reflections/', views.reflections, name='reflections'),
    path('publications/', views.publications, name='publications'),
    path('measurements/',views.measurements,name='measurements'),
    path('makers/', views.makers, name='makers'),
    path('iconography/', views.iconography, name='iconography'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('acknowledgements/', views.acknowledgements, name='acknowledgements'),
    path('collectionlinks/', views.collectionlinks, name='collectionlinks'),
    path('librarylinks/', views.librarylinks, name='librarylinks'),

]




