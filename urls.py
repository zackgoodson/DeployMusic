from django.urls import path
from .views import bandsPageView
from .views import singleBandPageView, addband, addbandPageView

urlpatterns = [
    path("bands/", bandsPageView, name="band"),
    path("<int:bandID>/", singleBandPageView, name="singleband"),
    path("addbandPageView/", addbandPageView, name="addbandPageView"), 
    path("addband/", addband, name="addband"), 
        
]