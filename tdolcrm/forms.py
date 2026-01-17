from django import forms 
from .models import Contact, Prospect , User, Invoice, Activities, Shipment_order, Lead, Shipment,Employee_Records, Campaign, Customer, Branch, Assortment,Case
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Column, Row, Field

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Contact
        fields = '__all__'


class CaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CaseForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Case
        fields = '__all__'

class ProspectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProspectForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Prospect
        fields = '__all__'

class InvoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InvoiceForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Invoice
        fields = ('__all__')

class ActivitiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActivitiesForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Activities
        fields = '__all__'

class ShipmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShipmentForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Shipment
        fields = ('__all__')

class LeadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LeadForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Lead
        fields = ('__all__')


class AssortmentForm(forms.ModelForm):

    class Meta:
        model = Assortment
        fields = ('__all__')

class CampaignForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CampaignForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Campaign
        fields = ('__all__')

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Row(
                    Div(
                    column(
                        Field('Last_Name', css_class='field-class'),
                        Field('First_Name', css_class = 'field-class'),
                    )
                )
            )
        )
        )

class EmployeerecordsForm(forms.ModelForm):

    class Meta:
        model = Employee_Records
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(Employee_Records).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['Departmentz'].queryset = Department.objects.all
        helper.form_class='form-horizontal'

    
class BranchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BranchForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Employee_Records
        fields = ('__all__')


class ShipmentorderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShipmentorderForm).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
    class Meta:
        model = Shipment_order
        fields = ('__all__')
