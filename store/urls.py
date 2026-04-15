from django.urls import path
from .views import home_page, register_page, login_page, dashboard_admin, \
    dealers_page, medicines_page, employees_page, customers_page, purchases_page,\
        confirm_logout_page, add_dealer_page, add_medicine_page, add_employee_page,\
            logout_page, add_customer_page, add_purchase_page, settings_page, update_dealer,\
                delete_dealer, update_medicine, delete_medicine, update_employee,\
                    delete_employee, update_customer, delete_customer, update_purchase,\
                        delete_purchase, register_admin, register_customer, \
                            login_admin, login_customer, dashboard_customer

app_name = 'store'

urlpatterns = [
    path('', home_page, name="home"),

    # Register Path
    path('register/', register_page, name="register"),
    path('register/admin/', register_admin, name="register-admin"),
    path('register/customer/', register_customer, name="register-customer"),
    
    # Login Path
    path('login/', login_page, name="login"),
    path('login/admin/', login_admin, name="login-admin"),
    path('login/customer/', login_customer, name="login-customer"),
    
    path('confirm-logout/', confirm_logout_page, name="confirm-logout"),
    path('confirm-logout/logout/', logout_page, name="logout"),
    path('dashboard/admin/', dashboard_admin, name="dashboard-admin"),
    path('dashboard/customer/', dashboard_customer, name="dashboard-customer"),

    # Dealer CRUD
    path('dealers/', dealers_page, name="view-dealers"),
    path('dealers/add-dealer/', add_dealer_page, name="add-dealer"),
    path('dealers/update-dealer/<int:pk>/', update_dealer, name="update-dealer"),
    path('dealers/delete-dealer/<int:pk>/', delete_dealer, name="delete-dealer"),

    # Medicine CRUD
    path('medicines/', medicines_page, name="view-medicines"),
    path('medicines/add-medicine/', add_medicine_page, name="add-medicine"),
    path('medicines/update-medicine/<int:pk>/', update_medicine, name="update-medicine"),
    path('medicines/delete-medicine/<int:pk>/', delete_medicine, name="delete-medicine"),
    
    # Employee CRUD
    path('employees/', employees_page, name="view-employees"),
    path('employees/add-employee/', add_employee_page, name="add-employee"),
    path('employees/update-employee/<int:pk>/', update_employee, name="update-employee"),
    path('employees/delete-employee/<int:pk>/', delete_employee, name="delete-employee"),

    # Customer CRUD
    path('customers/', customers_page, name="view-customers"),
    path('customers/add-customer/', add_customer_page, name="add-customer"),
    path('customers/update-customer/<int:pk>/', update_customer, name="update-customer"),
    path('customers/delete-customer/<int:pk>/', delete_customer, name="delete-customer"),

    # Purchase CRUD
    path('purchases/', purchases_page, name="view-purchases"),
    path('purchases/add-purchase/', add_purchase_page, name="add-purchase"),
    path('purchases/update-purchase/<int:pk>/', update_purchase, name="update-purchase"),
    path('purchases/delete-purchase/<int:pk>/', delete_purchase, name="delete-purchase"),

    path('settings/', settings_page, name="settings")
]