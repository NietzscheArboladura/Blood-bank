from django.urls import path
from myapp1 import views

app_name = 'myapp1'

urlpatterns = [

    path('', views.MyIndexView.as_view(), name="my_index_view"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard_view"),
    # To replace "success page" and default the index page with '' (blank).
    path('index/', views.MyIndexView.as_view(), name="my_index_view"), #Specifies the path for index.html
    # Name the attribute of the path the same as the class but with underscores: "my_index_view"
    # MyIndexView is the name of the class from views.py
    # Create/Specify one path for everytime you want to render/view a html file in a browser
    path('features/', views.FeaturesView.as_view(), name="features_view"),
    path('aboutus/', views.AboutView.as_view(), name="aboutus_view"),
    path('contactus/', views.ContactView.as_view(), name="contactus_view"),
    path('signup/', views.SignUpView.as_view(), name="signup_view"),
    path('signin/', views.SignInView.as_view(), name="signin_view"),
    path('createPatient/', views.CreatePatientView.as_view(), name="createpatient_view"),
    path('createPhlebotomist/', views.CreatePhlebotomistView.as_view(), name="createphlebotomist_view"),
    path('createLocation/', views.CreateLocationView.as_view(), name="createlocation_view"),
    path('rolefinalization/', views.RoleFinalizationView.as_view(), name="rolefinalization_view"),
    path('addDonor/', views.AddDonorView.as_view(), name="addDonor_view"),
    path('addDonation/', views.AddDonationView.as_view(), name="addDonation_view"),
    path('addTransaction/', views.AddTransactionView.as_view(), name="addTransaction_view"),
    path('logout/', views.logout, name='logout')
]