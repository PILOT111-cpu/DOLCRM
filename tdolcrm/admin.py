from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

from .models import Contact
from .models import Prospect 
from .models import Customer
from .models import Shipment_order
from .models import Shipment
from .models import Assortment
from .models import Case 
from .models import Employee_Records, Branch , Campaign , Activities , Invoice , User, Lead, Role, Department


class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'First_Name', 'Last_Name', 'Email_Address', 'Company_Name')
admin.site.register(Contact, ContactAdmin)

class ProspectAdmin(admin.ModelAdmin):
    list_display = ( 'First_Name', 'Last_Name', 'Email_Address', 'Company_Name')
admin.site.register(Prospect, ProspectAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ( 'First_Name', 'Last_Name', 'Email_Address', 'Company_Name')
admin.site.register(Customer, CustomerAdmin)

class Shipment_orderAdmin(admin.ModelAdmin):
    list_display = ('Consignee_telephone', 'No_of_packages', 'Item_description')
admin.site.register(Shipment_order, Shipment_orderAdmin)

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('Tracking_id', 'Shipmentorder1')
admin.site.register(Shipment, ShipmentAdmin)

class AssortmentAdmin(admin.ModelAdmin):
  list_display = ('Assortment_ID', 'Customer_Name', 'Assort_description', 'Item_label', 'pictures', 'uploaded_at', 'shipmentorder', 'AMOUNT_OF_QTY_SHIPPED', 'pictures_item', 'item_pictures', 'items_nums')
admin.site.register(Assortment, AssortmentAdmin)

class CaseAdmin(admin.ModelAdmin):
    list_display = ('Date_processed', 'Case_description', 'Case_Categories')
admin.site.register(Case, CaseAdmin)

class Employee_RecordsAdmin(admin.ModelAdmin):
    list_display = ('Employee_Name', 'Employment_date','Resumption_date')
admin.site.register(Employee_Records, Employee_RecordsAdmin)

class BranchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Branch, BranchAdmin)

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('Date_created', 'Start_date', 'End_date', 'Budget', 'Actual_cost', 'Expected_revenue')
admin.site.register(Campaign, CampaignAdmin)

class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('Activity_name', 'Date_created1','Start_date1','End_date1')
admin.site.register(Activities, ActivitiesAdmin)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('Invoice_ID', 'Consignee_Name_inv', 'Invoice_date', 'Shipment_origin', 'Total_Billable_weight')
admin.site.register(Invoice, InvoiceAdmin)

class LeadAdmin(admin.ModelAdmin):
    list_display = ( 'First_Name', 'Last_Name', 'Email_Address', 'Company_Name','Leads')

admin.site.register(Lead, LeadAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('Name')
admin.site.register(Role)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('Name')
admin.site.register(Department)


#admin.site.register(User)
