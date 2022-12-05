#(models.py)
from django.db import models

# Create your models here.
# The tables will be created here, not in the phpMyAdmin database
# 'makemigrations' command to save the contents here
# model inherits models.Model

#new table
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 20, unique=True)
    password = models.CharField(max_length = 20)

    class meta:
        db_table = 'Users'

    def __str__(self):
        return self.username

class Donors(models.Model):
    donor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    contact_number = models.CharField(max_length = 20)
    blood_type = models.CharField(max_length = 3)

    class meta: # Specifies the table name; For consistency, class name and table name are the same.
        db_table = 'Donors' 

class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,to_field='username',on_delete = models.CASCADE) #foreign key syntax
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    contact_number = models.CharField(max_length = 20)
    blood_type = models.CharField(max_length = 3)

    class meta:
        db_table = 'Patients' 

class Phlebotomists(models.Model):
    pbt_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,to_field='username',on_delete = models.CASCADE) #foreign key syntax
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    contact_number = models.CharField(max_length = 20)

    class meta:
        db_table = 'Phlebotomists' 
        
class Donations(models.Model):
    donation_id = models.AutoField(primary_key=True)
    donor_id = models.ForeignKey(Donors, on_delete = models.CASCADE)
    date_of_donation = models.DateField()
    amount = models.IntegerField()

    # class meta:
    #     db_table = 'Donations' 

class Donation_Transaction(models.Model):
    dt_id = models.AutoField(primary_key=True)
    pbt_id = models.ForeignKey(Phlebotomists, on_delete = models.CASCADE)
    patient_id = models.ForeignKey(Patients, on_delete = models.CASCADE)
    amount = models.IntegerField()
    date_donated = models.DateField()
    donation_id = models.ForeignKey(Donations, on_delete = models.CASCADE)
    blood_type = models.CharField(max_length = 3)

    class meta:
         db_table = 'Donation_Transaction' 

class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    dt_id = models.ForeignKey(Donation_Transaction, on_delete = models.CASCADE)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 20) 
    date_of_transaction = models.DateField()
    
    class meta:
        db_table = 'Location'


