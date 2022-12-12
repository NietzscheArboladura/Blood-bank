from django import forms
from .models import *

class PatientsForm(forms.ModelForm):
	class Meta:
		model = Patients
		fields= '__all__'

class PhlebotomistsForm(forms.ModelForm):
	class Meta:
		model = Phlebotomists
		fields= '__all__'

class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields= '__all__'

class DonationTransactionForm(forms.ModelForm):
	class Meta:
		model = Donation_Transaction
		fields= '__all__'

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields= '__all__'		

class DonorsForm(forms.ModelForm):

    class Meta:
        model = Donors
        fields= '__all__'