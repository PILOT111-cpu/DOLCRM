from django.urls import path, include 
from .import views 
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from tdolcrm import views
#from tdolcrm.views import ContactPage, CasePage, ActivitiesPage, BranchPage, CampaignPage, EmployeerecordsPage, InvoicePage, LeadsPage, ProspectPage, ShipmentsPage, ShipmentorderPage, CustomerPage, AssortmentPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tdolcrm.urls')),
    path('', include ('django.contrib.auth.urls')),
    path('account/', include('django.contrib.urls')),
   # path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chaining/', include('smart_selects.urls')), 

]