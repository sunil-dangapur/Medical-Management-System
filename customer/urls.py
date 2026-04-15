from django.urls import path
from .views import medicines_page, add_medicine_page, update_medicine, \
    delete_medicine, purchases_page, add_purchase_page, update_purchase, \
        delete_purchase, orders_page, add_order_page, update_order_page, \
            delete_order_page

app_name = "customer"

urlpatterns = [

    # Order CRUD
    path('orders/', orders_page, name="view-orders"),
    path('orders/add-order/', add_order_page, name="add-order"),
    path('orders/update/<int:pk>/', update_order_page, name="update-order"),
    path('orders/delete-order/<int:pk>/', delete_order_page, name="delete-order"),

    # Medicine CRUD
    path('medicines/', medicines_page, name="view-medicines"),
    path('medicines/add-medicine/', add_medicine_page, name="add-medicine"),
    path('medicines/update-medicine/<int:pk>/', update_medicine, name="update-medicine"),
    path('medicines/delete-medicine/<int:pk>/', delete_medicine, name="delete-medicine"),

    # Purchase CRUD
    path('purchases/', purchases_page, name="view-purchases"),
    path('purchases/add-purchase/', add_purchase_page, name="add-purchase"),
    path('purchases/update-purchase/<int:pk>/', update_purchase, name="update-purchase"),
    path('purchases/delete-purchase/<int:pk>/', delete_purchase, name="delete-purchase"),
]
