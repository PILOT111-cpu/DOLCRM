from django.db import models

# Create your models here.
from django.utils.text import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.urls import reverse
from datetime import datetime
from django_countries.fields import CountryField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

#class User(AbstractUser):
 #   pass

class Contact (models.Model): 
    #id = models.AutoField(primary_key=True,default=20)
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Email_Address = models.EmailField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Address_1=models.TextField(max_length=250, verbose_name='Address')
    Birthdate=models.DateField()

class Prospect (Contact):
    Nature_of_Business = models.CharField(max_length=50, verbose_name='Nature of Business')
    Nature_of_Shipment = models.CharField(max_length=50)
    Pickup_location = models.CharField(max_length=200)
    NoOfPackages_Monthly = models.IntegerField(verbose_name='No of Packages Monthly')
    Monthly_revenue = models.IntegerField(verbose_name='Monthly Revenue')

    def __str__(self):
        self.full_name = self.First_Name + " " + self.Last_Name
        return self.full_name

class Customer (Prospect):
    Customer_ID = models.BigAutoField (primary_key=True)
    Consignee_Name = models.CharField(max_length=50, verbose_name='Customer Name')
    Consignee_Company = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    No_of_packages_monthly = models.IntegerField(null=True)

class Branch (models.Model):
    Branches = (
        ('Ikeja' , 'Ikeja' ),
        ('Gbagada', 'Gbagada'),
        ('Surulere', 'Surulere'),
    )
    ##################################################################################################
    branches_loc = models.CharField(max_length=8, choices=Branches)

#Create Models for Chained Dropdown list:

class Department (models.Model):
    Name = models.CharField(max_length=50, verbose_name= 'Role')

    def __str__(self):
        return self.Name

class Role (models.Model):
    Name = models.CharField(max_length=50, verbose_name='Department')
    Department  = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Employee_Records (models.Model):
    Manager = (
        ('Business Manager', 'Business Manager'),
        ('Business Development Manager', 'Business Develoment Manager'),
    )

    Employment_validity1 = (
        ('Probation', 'Probation'),
        ('Confirmed', 'Confirmed'),
    )
    Branches = (
        ('Ikeja' , 'Ikeja' ),
        ('Gbagada', 'Gbagada'),
        ('Surulere', 'Surulere'),
    )
    
    Employee_ID = models.CharField(primary_key=True, default="4", max_length=4, verbose_name="Employee ID Code")
    Employee_Name = models.CharField(max_length=100)
    Rolez = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Role", max_length=50)
    Departmentz = models.ForeignKey(Department, on_delete=models.CASCADE,verbose_name='Department')
    Manager_Team= models.CharField(max_length=35, choices = Manager, verbose_name='Manager / Team Lead' )
    Employment_date = models.DateField(verbose_name="Hired Date")
    Resumption_date = models.DateField()
    Employment_Validity=models.CharField(choices=Employment_validity1, max_length=10)
    Employee_branch1 = models.CharField(choices=Branches, max_length=15, verbose_name='branch')
    
    def __str__(self):
        return self.Employee_Name

   # Branch_of_employee = models.OneToOneField(Branch, on_delete=models.CASCADE, verbose_name='Branch', default="")
    # create a relationship between the employee_records and the branch (one to one rel)

class Shipment_order(Customer):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    Tracking_number = models.CharField(primary_key=True, verbose_name='Tracking Number', default=1, max_length=18)
    Consignee_telephone = models.IntegerField(verbose_name='Consignee Telephone')
    No_of_packages = models.IntegerField()
    Dimensional_weight = models.IntegerField()
    Dimensional_height = models.IntegerField()
    Item_description = models.TextField(max_length=250)
    Customer_signature = models.CharField(max_length=250)
    Country_shipment = CountryField(blank_label = "(select country)", verbose_name= 'Country' ,default="") #consignee Country
   # Branch_of_shipment = models.OneToOneField(Branch, on_delete=models.CASCADE, related_name='', verbose_name='Shipment Branch', default="") #this generated an error without the @related_name
    Postal_code = models.IntegerField(default="1")
    Country_sender = CountryField(blank_label = "(select country)", verbose_name= 'Country' ,default="")
    Senders_FirstName = models.CharField(max_length=250 , verbose_name= 'First Name', default="")
    Senders_LastName = models.CharField(max_length=250, verbose_name= 'Last Name', default="")
    Total_weight = models.IntegerField(verbose_name = 'Total Weight' , default=0)
    length = models.IntegerField(default=0)
    Height= models.IntegerField(default=0)
    Weight= models.IntegerField(default=0)

    Branches = (
        ('Ikeja' , 'Ikeja' ),
        ('Gbagada', 'Gbagada'),
        ('Surulere', 'Surulere'),
    )
    ##################################################################################################
    Branch_of_shipment = models.CharField(max_length=8, choices=Branches, verbose_name='Shipment Branch')

   # def __str__(self):
    #    self.full_name = self.First_Name + " " + self.Last_Name 
     #   return  self.full_name 
# this is to test 

class Lead (Contact):
    Lead_Source = (
        ('Coldcall', 'Coldcall'),
        ('Campaign', 'Campaign'),
        ('Email', 'Email'),
        ('Word of Mouth', 'Word of Mouth'),
        ('Website', 'Website'),
        ('Tradeshow', 'Tradeshow'), 
        ('Direct mail', 'Direct mail'),
        ('Employee referral', 'Employee referral'),
        ('Self generated', 'Self generated'),
        ('Existing customer', 'Existing customer'),
        ('Other', 'Other',)
    )

    Leads = models.CharField(max_length=25, choices=Lead_Source, verbose_name='Lead source')
    # associate a Lead to a Sales Resource
    # associate a Lead to a Customer Service Executive
    def __str__(self):
        self.full_name = self.First_Name + " " + self.Last_Name
        return self.full_name


class Shipment(models.Model):
    Tracking_id = models.IntegerField(primary_key=True)
    Shipmentorder1 = models.OneToOneField(Shipment_order, on_delete=models.CASCADE, related_name='ships', verbose_name='Order ID')
    # SPECIFY OTHER FIELDS TO IDENTIFY THIS SHIPMENT WITH A CUSTOMER 
    Consignee_name1 = models.OneToOneField(Shipment_order, on_delete=models.CASCADE, verbose_name = 'consignee Name', default="")

    EscalationReasons = (
        ('MISDECLARATION' ,'Misdeclaration'),
        ('THEFT', 'Theft'),
        ('Delays', 'Delays'),
        ('Specify Others', 'Specify Others'),
    )
    Escalation = models.CharField(max_length=20, choices=EscalationReasons)

class Assortment (models.Model):
    #Assortment_ID = models.IntegerField(primary_key=True, verbose_name= 'Assortment ID', default='1')
    uploaded_at = models.DateTimeField(auto_now_add=True) #specific time the assortment was completed
    Assortment_ID = models.IntegerField(primary_key=True, verbose_name='Assortment ID')
    Customer_Name = models.OneToOneField(Customer, on_delete=models.CASCADE, max_length=1000)
    Assort_description = models.CharField(max_length=1000) #short description
    Dimensional_weight1=models.IntegerField(verbose_name= 'Dimensional Weight')
    Actual_weight1=models.IntegerField(verbose_name='Actual Weight')
    pictures = models.FileField()  # Upload image for the entire parcel upon arrival ---ADD IMAGE OF PARCEL
    Item_label = models.CharField(max_length=30) #name of each item 
    shipmentorder = models.OneToOneField(Shipment_order, on_delete=models.CASCADE, related_name= 'topic_content_type')
    AMOUNT_OF_QTY_SHIPPED = models.IntegerField(verbose_name='Quantityf') #quantity of each item
    pictures_item = models.FileField() # upload of each item in the box  "ITEM PACKAGE 1"
    item_pictures = models.FileField( verbose_name='Upload Image') # To upload specific items in the parcel brought in
    items_num = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'), 
        ('5', '5'),
        ('6', '6'),
        ('7', '7'), 
        ('8', '8'),
        ('9', '9'), 
        ('10', '10'),
    )
    items_nums = models.IntegerField(choices=items_num)

    class Item_qty(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10

    AMOUNT_OF_QTY_SHIPPED= models.IntegerField(choices=Item_qty.choices)

#class Shipment (models.Model):
 #   Tracking_No = models.IntegerField()

 #this assigns a shipment to many Cases. 

class Case(models.Model):
    Date_processed = models.DateTimeField()
    Case_description = models.CharField(max_length=500)
    Shipments = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    Case_Categories = models.OneToOneField(Shipment, on_delete=models.PROTECT, related_name='categories')

# This is a record of all employees. It will be expounded upon after further meeting with the HR Officers

class Designations (models.Model):
    Designation = (
        
        ('Customer Service Executive', 'Customer Service Executive'),
        ('Human Resources', 'Human Resources'),
        ('Sales Resource', 'Sales Resource'),
        ('Operations Officer', 'Operations Officer'),
        ('Marketing Officer', 'Marketing Officer'),
        ('Management', 'Management'),
    )

    Designations = models.CharField(max_length=30, choices=Designation)


class Sales_Resource(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)

class Customer_Service_Executive(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email

class Human_Resource(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
   
    #include branch as a choice

class Campaign(models.Model):
    Campaign_ID = models.IntegerField(primary_key=True, default=1)
    Campaign_Name = models.CharField(max_length=200)
    Date_created = models.DateTimeField()
    Start_date = models.DateField()
    End_date = models.DateField()
    Budget = models.IntegerField()
    Actual_cost = models.IntegerField()
    Expected_revenue = models.IntegerField()
    Campaign_objective = models.TextField(max_length=200)
    Campaign_description = models.TextField(max_length=300)

    def __str__(self):
        return self.Campaign_Name
    
class Activities (models.Model):
    Activity_name = models.CharField(max_length=100)
    Date_created1=models.DateField(verbose_name= 'Date Created')
    Start_date1=models.DateField(verbose_name='Start Date')
    End_date1=models.DateField(verbose_name =' End Date')
    Employee_assigned = models.ForeignKey(Employee_Records, on_delete=models.CASCADE, verbose_name= 'Employee Assigned')
    Activity_description = models.TextField(max_length=300, verbose_name='Activity description')
    Campaign_Activities = models.ForeignKey(Campaign, on_delete=models.PROTECT, verbose_name='Campaign Name')

    def __str__(self):
        return self.Activity_name
    
class Invoice (models.Model):
    Invoice_ID = models.IntegerField(primary_key=True)
    AssortmentIDs = models.OneToOneField(Assortment, on_delete=models.PROTECT, verbose_name='Assortment ID')
    Consignee_Name_inv = models.OneToOneField(Customer, on_delete = models.PROTECT, verbose_name='Sender Name')
    Invoice_date = models.DateTimeField(auto_now_add=True, verbose_name='Invoice Date')
    Shipment_origin = CountryField(blank_label = "(select country)", verbose_name= 'Shipment Origin')
    No_of_packages1 = models.IntegerField(verbose_name='No of Packagees')
    Total_Billable_weight = models.IntegerField(verbose_name='Total Billable Weight')
    Tracking_numbers = models.OneToOneField(Shipment, on_delete = models.PROTECT, verbose_name='Tracking Number')
    Insurance_choice = (
        ('Yes', 'Yes'),
        ('No' , 'No'),
    )
    Insurances = models.CharField(max_length=3 ,choices=Insurance_choice)
    Packaging_fee = models.IntegerField()
    Freight_cost = models.IntegerField()
    Total_shipment_cost = models.IntegerField()
    Date_created3 = models.DateTimeField(verbose_name= 'Date Created', default='2012-09-04 18:00')
    Assortment_IDs_Inv = models.OneToOneField(Assortment,on_delete=models.CASCADE, verbose_name='Assortment ID', related_name= 'topic_content_type', default=1)

