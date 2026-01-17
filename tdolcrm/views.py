from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from tdolcrm.models import * 
from django import forms
from .forms import ContactForm, ShipmentForm, InvoiceForm , BranchForm , LeadForm, ProspectForm, CampaignForm, ShipmentorderForm, CaseForm, EmployeerecordsForm , AssortmentForm, LeadForm, ActivitiesForm
from django.forms import ModelForm
from django.http import HttpResponsePermanentRedirect, HttpResponse
#from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import generic
from .  import models    #############################################COME BAACK TO THIS LATER
from django.contrib.messages.views import SuccessMessageMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
#from .models import Contact, Branch

# create a view for each of the lists 
def Activities_list(request):
    activities = Activities.objects.all()
    return render(request, 'tdolcrm/listActivities.html', {'activities':activities})

def Contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'tdolcrm/listContact.html', {'contacts':contacts})

def Assortments_list(request):
    assortments = Assortment.objects.all()
    return render(request, 'tdolcrm/listAssortment.html', {'assortments': assortment})

def Cases_list(request):
    cases = Case.objects.all()
    return render(request, 'tdolcrm/listCases.html', {'cases': cases})

def Customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'tdolcrm/listCustomer.html', {'customers':customers})

def Employeerecords_list(request):
    employeerecords=Employee_Records.objects.all()
    return render(request, 'tdolcrm/listEmployeerecords.html', {'employeerecords':employeerecords})

def Leads_list(request):
    leads = Lead.objects.all()
    return render(request, 'tdolcrm/listleads.html', {'leads':leads})

def Prospects_list(request):
    prospects = Prospect.objects.all()
    return render(request, 'tdolcrm/listProspect.html', {'prospects':prospects})

def Shipments_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'tdolcrm/listShipment.html', {'shipments':shipments})

def Invoices_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'tdolcrm/listInvoice.html', {'invoices':invoices})

def Shipmentorders_list(request):
    shipmentorders = Shipment_order.objects.all()
    return render(request, 'tdolcrm/listShipmentorder.html', {'shipmentorders':shipmentorders})

def Campaigns_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'tdolcrm/listCampaign.html', {'campaigns':campaigns})

def contact_record(request, pk):
    contact_record = Contact.objects.get(id=pk)
    return render(request, 'tdolcrm2/contactrecord.html', {'contact_record':contact_record})
    messages.success(request, "you must be loggedin to view user")
    return redirect('home')

def activity_record(request, pk):
    if request.user.is_authenticated:
        activity_record = Activities.objects.get(id=pk)
        return render(request, 'tdolcrm2/activitiesrecord.html', {'activity_record':activity_record})
    else:
        messages.success(request, "you must be loggedin to view user")
        return redirect('home')

def assortment_record(request, pk):
    if request.user.is_authenticated:
        assortment_record = Assortment.objects.get(id=pk)
        return render(request, 'tdolcrm2/assortmentrecord.html', {'assortment_record':assortment_record})
    else:
        messages.success(request, "you must be loggedin to view user")
        return redirect('home')

def case_record(request, pk):
    if request.user.is_authenticated:
        case_record = Case.objects.get(id=pk)
        return render(request, 'tdolcrm2/caserecord.html', {'case_record':case_record})
    else:
        messages.success(request, "you must be loggedin to view user")
        return redirect('home')

def employee_record(request, pk):
    if request.user.is_authenticated:
        employee_record = Employee_Records.objects.get(id=pk)
        return render(request, 'tdolcrm2/employeerecord.html', {'employee_record':employee_record})
    else:
        messages.success(request, "you must be logged in to view user")
        return redirect('home')

def invoice_record(request, pk):
    if request.user.is_authenticated:
        invoice_record = Invoice.objects.get(id=pk)
        return render(request, 'tdolcrm2/invoicerecord.html', {'invoice_record':invoice_record})
    else:
        messages.success(request, "you must be loggedin to view user")
        return redirect('home')

def lead_record(request, pk):
    lead_record = Lead.objects.get(id=pk)
    return render(request, 'tdolcrm2/leadrecord.html', {'lead_record':lead_record})
    messages.success(request, "you must be loggedin to view user")
    return redirect('home')

def prospect_record(request, pk):
    prospect_record = Prospect.objects.get(id=pk)
    return render(request, 'tdolcrm2/prospectrecord.html', {'prospect_record':prospect_record})
    messages.success(request, "you must be loggedin to view user")
    return redirect('home')

def campaign_record(request, pk):
    campaign_record = Campaign.objects.get(id=pk)
    return render(request, 'tdolcrm2/campaignrecord.html', {'campaign_record':campaign_record})
    messages.success(request, "you must be loggedin to view user")
    return redirect('home')

def shipmentorder_record(request, pk):
    if request.user.is_authenticated:
        shipmentorder_record = Shipment_order.objects.get(id=pk)
        return render(request, 'tdolcrm2/shipmentorderrecord.html', {'shipmentorder_record':shipmentorder_record})
    else:
        messages.success(request, "you must be loggedin to view user")
        return redirect('home')

def shipment_record(request, pk):
    if request.user.is_authenticated:
        shipment_record = Shipment.objects.get(id=pk)
        return render(request, 'tdolcrm2/shipmentorderrecord.html', {'shipmentorder_record':shipmentorder_record})
    else:
        messages.success(request, "you must be loggedin to view user")
        return redirect('home')

#this is the view that handles authentication, if the correct credientials are entered, take the user to the home page 
def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username= username, password= password)
        
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
             # Authentication failed, display an error message
            message = "Invalid username or password."
            return render(request, 'registration/success.html', {'message': message})

    return render(request, 'registration/login.html')

#for you to enter the home page login is required. 

def home(request):
    return render(request, "registration/login.html",{})

#@login_required(login_url ='/log-in/')
def ContactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully saved a contact")
            return redirect ('contact-list')
    else:
        form = ContactForm()
    return render(request, 'tdolcrm/Contacts.html', {'form':form})

def CasePage (request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully saved Case!")
            return redirect ('cases-list')
    else:
        form = CaseForm()
    return render(request, 'tdolcrm/cases.html', {'form':form})

# create view for success page
#@login_required  
def SuccessPage(request):
    return render(request, 'registration/success.html', {})

def ActivitiesPage (request):
    if request.method == 'POST':
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully saved an Activity")
            return redirect('activities-list')
        else:
            print (form.errors)
          #  return HttpResponseRedirect('login')
    else:
        form = ActivitiesForm()
    return render(request, 'tdolcrm/activities.html', {'form':form})

def BranchPage (request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
        #    return HttpResponseRedirect('login')
    else:
        form = BranchForm()
    return render(request, 'tdolcrm/branch.html', {'form':form})


def CampaignPage (request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully entered a Campaign")
            return redirect('campaigns-list')
          #  return HttpResponseRedirect('login')
    else:
        form = CampaignForm()
    return render(request, 'tdolcrm/Campaigns.html', {'form':form})

def EmployeerecordsPage (request):
    if request.method == 'POST':
        form = EmployeerecordsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully entered an Employee")
            return redirect('employeerecords-list')
    else:
        form = EmployeerecordsForm()
    return render(request, 'tdolcrm/employeerecords.html', {'form':form})

def InvoicePage (request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully entered an Invoice")
            return redirect('invoices-list')
           # return HttpResponseRedirect('login')
    else:
        form = InvoiceForm()
    return render(request, 'tdolcrm/invoice.html', {'form':form})

def LeadsPage (request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully entered a Lead")
            return redirect('leads-list')
         #   return HttpResponseRedirect('login')
    else:
        form = LeadForm()
    return render(request, 'tdolcrm/leads.html', {'form':form})

def ProspectPage (request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully entered a Prospect")
            return redirect('prospects-list')
          #  return HttpResponseRedirect('login')
    else:
        form = ProspectForm()
    return render(request, 'tdolcrm/prospect.html', {'form':form})

def ShipmentsPage (request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully entered a Shipment")
            return redirect('shipments-list')
           # return HttpResponseRedirect('login')
    else:
        form = ShipmentForm()
    return render(request, 'tdolcrm/shipment.html', {'form':form})

def ShipmentorderPage (request):
    if request.method == 'POST':
        form = ShipmentorderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully entered an Order")
            return redirect ('shipmentorders-list')
          #  return HttpResponseRedirect('login')
    else:
        form = ShipmentorderForm()
    return render(request, 'tdolcrm/shipmentorder.html', {'form':form})

def CustomerPage (request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully entered a Customer")
            return redirect ('customers-list')
          #  return HttpResponseRedirect('login')
    else:
        form = CustomerForm()
    return render(request, 'tdolcrm/customer.html', {'form':form})

def AssortmentPage(request):
    if request.method =='POST':
        form = AssortmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully entered an Asssortment")
            return redirect ('assortments-list')
    else:
        form = AssortmentForm()
    return render(request, 'tdolcrm/assortment.html',{'form':form})


class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = ['id', 'Last_Name', 'First_Name', 'Email_Address', 'Company_Name', 'Address_1','Birthdate']
        widgets = {
            'Birthdate': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 


class CaseForm(ModelForm):
    
    class Meta:
        model = models.Case
        fields = ['Date_processed', 'Case_description', 'Shipments', 'Case_Categories']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class ProspectForm(ModelForm):
    class Meta:
        model = models.Prospect
        fields = ['Last_Name', 'First_Name', 'Email_Address', 'Company_Name', 'Address_1', 'Birthdate', 'Nature_of_Business', 
        'Nature_of_Shipment', 'Pickup_location', 'NoOfPackages_Monthly', 'Monthly_revenue']
        widgets= {
            'Birthdate':forms.widgets.DateInput(attrs={'type': 'date'})
        }


    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 


class ActivitiesForm(ModelForm):
    Date_processed = forms.DateField(
       label = 'Date processed'
    )
    class Meta:
        model = models.Activities
        fields = ['Activity_name', 'Date_created1', 'Start_date1', 'End_date1', 'Employee_assigned', 'Activity_description', 'Date_processed', 'Campaign_Activities']
        widgets = {
            'Date_created1':forms.widgets.DateInput(attrs={'type': 'date'}),
            'Start_date1':forms.widgets.DateInput(attrs={'type': 'date'}),
            'End_date1':forms.widgets.DateInput(attrs={'type': 'date'}),
            
        }
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 


class InvoiceForm(ModelForm):
  #  Date_processed = forms.CharField(
   #     label = 'Date processed'
    #)
    Consignee_Name_inv = forms.CharField(
        label = 'Consignee name'
    )
    No_of_packages1 = forms.CharField(
        label = 'No of packages'
    )
    class Meta:
        model = models.Invoice
        fields = ['Invoice_ID', 'AssortmentIDs','Consignee_Name_inv', 'Shipment_origin','No_of_packages1', 'Total_Billable_weight', 'Tracking_numbers', 'Insurances', 'Packaging_fee', 
        'Freight_cost', 'Total_shipment_cost', 'Date_created3']
        widgets = {
            'Date_created3': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class LeadForm(ModelForm):
  
    class Meta:
        model = models.Lead
        fields = ['Last_Name', 'First_Name', 'Email_Address', 'Company_Name', 'Address_1', 'Birthdate', 'Leads']
        widgets = {
            'Birthdate': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class EmployeerecordsForm(ModelForm):
    class Meta:
        model = models.Employee_Records
        fields = ['Employee_Name','Departmentz','Rolez', 'Manager_Team', 'Employment_date', 'Resumption_date', 'Employment_Validity', 'Employee_branch1']
        widgets = {
            'Employment_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'Resumption_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class BranchForm(ModelForm):
    Date_processed = forms.CharField(
        label = 'Date processed'
    )
    class Meta:
        model = models.Branch
        fields = ['branches_loc']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class CustomerForm(ModelForm):
    Date_processed = forms.CharField(
        label = 'Date processed'
    )
    class Meta:
        model = models.Customer
        fields = ['Last_Name', 'First_Name', 'Email_Address', 'Company_Name', 'Address_1', 'Birthdate', 'Nature_of_Business', 'Nature_of_Shipment'
        ,'Pickup_location', 'NoOfPackages_Monthly', 'Monthly_revenue', 'Consignee_Name', 'Consignee_Company', 'Address',  'No_of_packages_monthly' ]
        widgets = {
            'Birthdate': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.form_class = 'form-horizontal'
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class CampaignForm(ModelForm):
    class Meta:
        model = models.Campaign
        fields = ['Campaign_Name', 'Date_created', 'Start_date', 'End_date', 'Budget', 'Actual_cost', 'Expected_revenue', 'Campaign_objective', 'Campaign_description']
        widgets = {
            'Date_created': forms.widgets.DateInput(attrs={'type': 'date'}),
            'Start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'End_date':forms.widgets.DateInput(attrs={'type': 'date'}),
        }
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class ShipmentForm(ModelForm):
    Shipmentorder1 = forms.CharField(
        label = 'Shipment order'
    )
    class Meta:
        model = models.Shipment
        fields = ['Tracking_id', 'Shipmentorder1', 'Escalation', 'Consignee_name1']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper

class ShipmentorderForm(ModelForm):
   # NoOfPackages_Monthly = forms.CharField(
    #    label = 'No of Packages Monthly'
    #)
    Address_1 = forms.CharField(
        label = 'Address'
    )
   
    class Meta:
        model = models.Shipment_order
        fields = ['Company_Name', 'Last_Name', 'First_Name','Email_Address', 'Consignee_telephone', 'No_of_packages', 'Country_shipment', 'Dimensional_weight', 'Address_1', 'Country_sender', 'Postal_code', 'Senders_FirstName', 'Senders_LastName','Item_description', 'Total_weight', 'length', 'Height', 'Weight' ]

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
          #  helper.field_class = 'col-3'
           # helper.label_class = 'col-9'
      #  helper.layout.append(Submit('submit', 'Submit', css_class='btn-success'))   
       
        return helper

#views for deleting records#######################################################################
def delete_contact(request, pk):
    delete_it=Contact.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record has been succesfully deleted")
    return redirect ('home')
    messages.success(request, "you must be logged in")
    return redirect('home')

def delete_prospect(request, pk):
    delete_it=Prospect.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record has been succesfully deleted")
    return redirect ('home')
    messages.success(request, "you must be logged in")
    return redirect('home')

def delete_lead(request, pk):
    delete_it=Lead.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record has been succesfully deleted")
    return redirect ('home')
    messages.success(request, "you must be logged in")
    return redirect('home')

def delete_campaign(request, pk):
    delete_it=campaign.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record has been succesfully deleted")
    return redirect ('home')
    messages.success(request, "you must be logged in")
    return redirect('home')

def delete_invoice(request, pk):
    delete_it=invoice.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Record has been succesfully deleted")
    return redirect ('home')
    messages.success(request, "you must be logged in")
    return redirect('home')








