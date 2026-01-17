"""tis URL Configuration

"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from tdolcrm import views
from tdolcrm.views import ContactPage, CasePage, ActivitiesPage, BranchPage, CampaignPage, EmployeerecordsPage, InvoicePage, LeadsPage, ProspectPage, ShipmentsPage, ShipmentorderPage, CustomerPage, AssortmentPage, SuccessPage, contact_record


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/add',views.ContactPage, name='contactz'),
    path('prospect/add',views.ProspectPage, name='prospect'),
    path('case/add',views.CasePage, name='case'),
    path('activities/add',views.ActivitiesPage, name='activity'),
    path('branch/add',views.BranchPage, name='branch'),
    path('campaign/add',views.CampaignPage, name='campaign'),
    path('invoice/add',views.InvoicePage, name='invoice'),
    path('shipment/add',views.ShipmentsPage, name='shipment'),
    path('customer/add',views.CustomerPage, name='customer'),
    path('shipmentorder/add',views.ShipmentorderPage, name='shipmentorder'),
    path('lead/add',views.LeadsPage, name='lead'),
    path('employeerecord/add',views.EmployeerecordsPage, name='employeerecord'),
    path('assortment/add', views.AssortmentPage, name = 'assortment'),
    path('log-in/', views.LoginPage, name ='login'),
    path('', views.home, name ='home'),
    #path('home/', views.home, name='home'), 
    path('success/', views.SuccessPage, name='success'),
    path('contact-list/', views.Contacts_list, name ='contact-list'),
    path('activities-list/', views.Activities_list, name ='activities-list'),
    path('assortments-list/', views.Assortments_list, name ='assortments-list'),
    path('cases-list/', views.Cases_list, name ='cases-list'),
    path('customers-list/', views.Customers_list, name ='customers-list'),
    path('employeerecords-list/', views.Employeerecords_list, name ='employeerecords-list'),
    path('leads-list/', views.Leads_list, name ='leads-list'),
    path('prospects-list/', views.Prospects_list, name ='prospects-list'),
    path('shipments-list/', views.Shipments_list, name ='shipments-list'),
    path('shipmentorders-list/', views.Shipmentorders_list, name ='shipmentorders-list'),
    path('campaigns-list/', views.Campaigns_list, name ='campaigns-list'),
    path('invoices-list/', views.Invoices_list, name ='invoices-list'),
    path('contacts/<int:pk>', views.contact_record, name ='contact_record'),
    #path for records display ###########################################################################################
    path('activities/<int:pk>', views.activity_record, name ='activity_record'),
    path('assortment/<int:pk>', views.assortment_record, name ='assortment_record'),
    path('campaign/<int:pk>', views.campaign_record, name ='campaign_record'),
    path('case/<int:pk>', views.case_record, name ='case_record'),
    path('contact/<int:pk>', views.contact_record, name ='contact_record'),
    path('employeerecord/<int:pk>', views.employee_record, name ='employee_record'),
    path('invoice/<int:pk>', views.invoice_record, name ='invoice_record'),
    path('lead/<int:pk>', views.lead_record, name ='lead_record'),
    path('prospect/<int:pk>', views.prospect_record, name ='prospect_record'),
    path('shipmentorderrecord/<int:pk>', views.shipmentorder_record, name ='shipmentorder_record'),
    path('shipmentrecord/<int:pk>', views.shipment_record, name ='shipment_record'),

    #path for deleting records ###################################################################################
    path('delete_contact/<int:pk>', views.delete_contact, name='delete_contact'),
    path('delete_prospect/<int:pk>', views.delete_prospect, name='delete_prospect'),
    path('delete_lead/<int:pk>', views.delete_lead, name='delete_lead'),
    path('delete_campaign/<int:pk>', views.delete_campaign, name = 'delete_campaign'),
    path('delete_invoice/<int:pk>', views.delete_campaign, name = 'delete_invoice')
]

admin.site.site_header = "TOLADOL".upper
