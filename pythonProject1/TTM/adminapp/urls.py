from django.urls import path
from . import views
urlpatterns = [
     path("ttmhome",views.ttmhome,name="ttmhome"),
     path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),
     path("checkRegistration", views.checkregistration,name="checkRegistration"),
     path("checkpackages", views.checkpackages,name="checkpackages"),
     path("viewpalaces",views.viewplaces,name="viewplaces"),
     path("changepassword",views.checkchangePassword,name="changepassword"),
     path("logout",views.logout,name="logout"),
]