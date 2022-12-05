from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.
class MyIndexView(View): 
    def get(self, request): 
        return render(request, 'pages/index.html', {})

class DashboardView(View): 
    def get(self, request):
        #changes here
        if 'user' in request.session:
            patients = Patients.objects.all()
            phlebotomists = Phlebotomists.objects.all()
            location = Location.objects.all()
            donation_transaction = Donation_Transaction.objects.all()
            current_user = request.session['user']
            context = {
                'patients' : patients,
                'phlebotomists' : phlebotomists,
                'location': location,
                'donation_transaction': donation_transaction,
                'current_user': current_user
            }
            return render(request, 'pages/dashboard.html', context)
        else:
            return HttpResponse('Please login first to view this page.') 
    def post(self, request):
       if request.method == 'POST':
            # no changes in update and delete (all tables)
            # Patients Table
            if 'btnUpdatePatient' in request.POST:
                print('Update button clicked!')
                pid = request.POST.get("patient_id")
                pfname = request.POST.get("first_name")
                plname = request.POST.get("last_name")
                pcnum = request.POST.get("contact_number")
                pbtype = request.POST.get("blood_type")
                update_Patient = Patients.objects.filter(patient_id=pid).update(first_name = pfname, last_name = plname, contact_number = pcnum, blood_type = pbtype)
                print(update_Patient)
                print('Patient record updated!')
            elif 'btnDeletePatient' in request.POST:
                print('Delete button clicked!')
                pid = request.POST.get("patient_id")
                Patients.objects.filter(patient_id=pid).delete()
                print("Patient record deleted")

            # Phlebotomists Table
            if 'btnUpdatePhlebotomist' in request.POST:
                print('Update button clicked!')
                phid = request.POST.get("pbt_id")
                phfname = request.POST.get("first_name")
                phlname = request.POST.get("last_name")
                phcnum = request.POST.get("contact_number")
                update_Phlebotomist = Phlebotomists.objects.filter(pbt_id=phid).update(first_name = phfname, last_name = phlname, contact_number = phcnum)
                print(update_Phlebotomist)
                print('Phlebotomist record updated!')
            elif 'btnDeletePhlebotomist' in request.POST:
                print('Delete button clicked!')
                phid = request.POST.get("pbt_id")
                Phlebotomists.objects.filter(pbt_id=phid).delete()
                print("Phlebotomist record deleted")

            # Locations Table
            if 'btnUpdateLocation' in request.POST:
                print('Update button clicked!')
                lid = request.POST.get("loc_id")
                lstate = request.POST.get("state")
                lcity = request.POST.get("city")
                lzipcode = request.POST.get("zip_code")
                ldot = request.POST.get("date_of_transaction")
                ldtid = request.POST.get("dt_id")
                update_Location = Location.objects.filter(loc_id=lid).update(dt_id= ldtid, state = lstate, city = lcity, zip_code = lzipcode, date_of_transaction = ldot)
                print(update_Location)
                print('Location record updated!')
            elif 'btnDeleteLocation' in request.POST:
                print('Delete button clicked!')
                lid = request.POST.get("loc_id")
                Location.objects.filter(loc_id=lid).delete()
                print("Location record deleted")

            return redirect('myapp1:dashboard_view')

class CreatePatientView(View):
    def get(self, request):
        #changes here
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user
            }
        return render(request, 'pages/createPatient.html',context)
    def post(self, request):        
        form = PatientsForm(request.POST, request.FILES)   
        #changes here with form.cleaned.data     
        if form.is_valid():
            # try:
            #pid = request.POST.get("patient_id")
            fk = form.cleaned_data.get("username")
            pfname = request.POST.get("first_name")
            plname = request.POST.get("last_name")
            pcnum = request.POST.get("contact_number")
            pbtype = request.POST.get("blood_type")
            form = Patients(username = fk, first_name = pfname, last_name = plname, contact_number = pcnum, blood_type = pbtype)
            form.save() 
            return redirect('myapp1:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class CreatePhlebotomistView(View):
    def get(self, request):
        #same changes with CreatePatientView
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user
            }
        return render(request, 'pages/createPhlebotomist.html',context)
    def post(self, request):        
        form = PhlebotomistsForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            fk = form.cleaned_data.get("username")
            phlfname = request.POST.get("first_name")
            phllname = request.POST.get("last_name")
            phlcnum = request.POST.get("contact_number")
            form = Phlebotomists(username = fk,first_name = phlfname, last_name = phllname, contact_number = phlcnum)
            form.save() 
            return redirect('myapp1:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

#no changes here
class CreateLocationView(View):
    def get(self, request):
        donation_transaction = Donation_Transaction.objects.all()
        context = {
            'donation_transaction': donation_transaction,
        }
        return render(request, 'pages/createLocation.html',context)
    def post(self, request):        
        form = LocationForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            lstate = request.POST.get("state")
            lcity = request.POST.get("city")
            lzipcode = request.POST.get("zip_code")
            ldot = request.POST.get("date_of_transaction")
            ldtid = request.POST.get("dt_id")
            fk = form.cleaned_data.get("dt_id")
            form = Location(state = lstate, city = lcity, zip_code = lzipcode, date_of_transaction = ldot, dt_id = fk)
            form.save() 
            return redirect('myapp1:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class FeaturesView(View): 
    def get(self, request): 
        return render(request, 'pages/features.html', {})

class AboutView(View): 
    def get(self, request): 
        return render(request, 'pages/aboutus.html', {})

class ContactView(View): 
    def get(self, request): 
        return render(request, 'pages/contactus.html', {})
#changes here and SignInView      
class SignUpView(View): 
    def get(self, request): 
        return render(request, 'pages/signup.html', {})
    def post(self, request):        
        form = UsersForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            if Users.objects.filter(username=username).count()>0:
                return HttpResponse('Username already exists.')
            else:
                form = Users(username = username, password = password)
                form.save()
                check_user = Users.objects.filter(username=username, password=password)
                if check_user:
                    request.session['user'] = username
                    return redirect('myapp1:rolefinalization_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')
        
class SignInView(View): 
    def get(self, request): 
        return render(request, 'pages/signin.html', {})
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            check_user = Users.objects.filter(username=username, password=password)
            if check_user:
                request.session['user'] = username
                return redirect('myapp1:dashboard_view')
            else:
                return HttpResponse('Please enter valid Username or Password.')
        return render(request, 'pages/signin.html', {})

#New View
class RoleFinalizationView(View):
    def get(self, request):
        if 'user' in request.session:
            current_user = request.session['user']
            context = {
                'current_user': current_user,
            }
            return render(request, 'pages/rolefinalization.html', context)
        else:
            return HttpResponse('Please login first to view this page.')


#logout code
def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('myapp1:signin_view')
    return redirect('myapp1:signin_view')

class AddDonorView(View):
    def get(self, request): 
        return render(request, 'pages/addDonor.html', {})
    def post(self, request):        
        form = DonorsForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            dfname = request.POST.get("first_name")
            dlname = request.POST.get("last_name")
            dcnum = request.POST.get("contact_number")
            dbtype = request.POST.get("blood_type")
            form = Donors(first_name = dfname, last_name = dlname, contact_number = dcnum, blood_type = dbtype)
            form.save() 
            return redirect('myapp1:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class AddDonationView(View):
    def get(self, request): 
        donors = Donors.objects.all()
        context = { 
            'donors': donors, 
        }
        return render(request, 'pages/addDonation.html', context)
    def post(self, request):        
        form = DonationsForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            dndate = request.POST.get("date_of_donation")
            dnamnt = request.POST.get("amount")
            request.POST.get("donor_id")  
            fkdnid = form.cleaned_data.get("donor_id")
            form = Donations(date_of_donation = dndate, amount = dnamnt, donor_id = fkdnid)
            form.save() 
            return redirect('myapp1:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')

class AddTransactionView(View):
    def get(self, request):
        pbt = Phlebotomists.objects.all()
        donations = Donations.objects.all()
        patients = Patients.objects.all()
        context = {
            'pbt': pbt, 
            'donations': donations,
            'patients': patients,
        }
        return render(request, 'pages/addTransaction.html', context)
    def post(self, request):        
        form = Donation_TransactionForm(request.POST, request.FILES)        
        if form.is_valid():
            # try:
            dtamnt = request.POST.get("amount")
            dtdate = request.POST.get("date_donated")
            dtbtype = request.POST.get("blood_type")
            request.POST.get("donation_id")
            request.POST.get("patient_id")  
            request.POST.get("pbt_id")  
            fkdnid = form.cleaned_data.get("donation_id")
            fkpttid = form.cleaned_data.get("patient_id")
            fkpbtid = form.cleaned_data.get("pbt_id")
            form = Donation_Transaction(amount = dtamnt, date_donated = dtdate, blood_type = dtbtype, donation_id = fkdnid, patient_id = fkpttid, pbt_id = fkpbtid)
            form.save() 
            return redirect('myapp1:dashboard_view')
        else:
            print(form.errors)
            return HttpResponse('not valid')