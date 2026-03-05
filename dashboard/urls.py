from django.urls import path

from dashboard.views import homePage

urlpatterns = [
    # path("homePage", homePage)
    path("", homePage)
    
]
 