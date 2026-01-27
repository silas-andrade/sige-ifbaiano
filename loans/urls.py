from django.urls import path

from .views import (
    RequestLoan,
    MakeLoanReturn, 
    DashboardUser, 
    DashboardAdmin, 
    ViewAllLoans, 
    BlockUser, 
    ViewMaterials, 
    DeleteMaterial, 
    AcceptMaterialReturn,
    AcceptLoanApplication,
    RejectLoanApplication
    )


app_name = 'loans'

urlpatterns = [
    
    path('request-loan/', RequestLoan, name='request-loan'),
    path('make-loan-return/', MakeLoanReturn, name='make-loan-return'),
    path('dashboard-user/', DashboardUser, name='dashboard-user'),
    path('dashboard-admin/', DashboardAdmin, name='dashboard-admin'),
    path('all-loans/', ViewAllLoans, name='all-loans'),
    path('block-user/<str:pk>/', BlockUser, name='block-user'),
    path('view-materials/', ViewMaterials, name='view-materials'),
    path('delete-material/<str:pk>/', DeleteMaterial, name='delete-material'),
    path('accept-material-return/<str:pk>/', AcceptMaterialReturn, name='accept-material-return'),
    path('accept-loan-application/<str:pk>/', AcceptLoanApplication, name='accept-loan-application'),
    path('reject-loan-application/<str:pk>/', RejectLoanApplication, name='reject-loan-application'),

]

