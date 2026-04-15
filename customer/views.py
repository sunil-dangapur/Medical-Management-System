from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from store.models import Medicine, Purchase
from .models import Order
from store.models import Purchase
from django.contrib import messages
from store.forms import AddMedicineForm, AddPurchaseForm,\
        UpdateMedicineForm, UpdateCustomerForm,\
                UpdatePurchaseForm, AddOrderForm, UpdateOrderForm


"""
Order CRUD Starts Here
"""
@login_required(login_url="/login/customer/")
def orders_page(request):
    orders = Order.objects.filter(customer=request.user)

    context = {
        "orders": orders
    }
    return render(request, "store/customer/view-orders.html", context)


@login_required(login_url="/login/customer/")
def add_order_page(request):
    form = AddOrderForm()

    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data.get("customer")
            med_name = form.cleaned_data.get("med_name")
            price = form.cleaned_data.get("price")
            quantity = form.cleaned_data.get("quantity")

            order = Order(
                customer=customer, med_name=med_name, 
                price=price, quantity=quantity
            )
            order.save()
            messages.success(request, "You have added a new order.")
            return redirect("customer:view-orders")
        return redirect("customer:add-order")
    
    context = {
        "form": form
    }
    return render(request, "store/customer/add-order.html", context)


@login_required(login_url="/login/customer/")
def update_order_page(request, pk):
    order = Order.objects.get(id=pk)
    form = AddOrderForm(instance=order)

    if request.method == "POST":
        form = AddOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "You have updated that order.")
            return redirect("customer:view-orders")
        return redirect("customer:add-order")

    context = {
        "form": form
    }
    return render(request, "store/customer/update-order.html", context)


@login_required(login_url="/login/customer/")
def delete_order_page(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    messages.success(request, "You have successfully deleted that order.")
    return redirect("customer:view-orders")

"""
Order CRUD Ends Here
"""

"""
Medicine CRUD Starts Here
"""
@login_required(login_url="/login/customer/")
def medicines_page(request):
    medicines = Medicine.objects.all()

    context = {
        "medicines": medicines
    }
    return render(request, "store/customer/view-medicines.html", context)


@login_required(login_url="/login/customer/")
def add_medicine_page(request):
    form = AddMedicineForm()

    if request.method == "POST":
        form = AddMedicineForm(request.POST)
        if form.is_valid():
            med_code = form.cleaned_data.get("med_code")
            med_name = form.cleaned_data.get("med_name")
            dealer_name = form.cleaned_data.get("dealer_name")
            price = form.cleaned_data.get("price")
            stock = form.cleaned_data.get("stock")
            description = form.cleaned_data.get("description")

            medicine = Medicine(
                med_code=med_code, med_name=med_name, dealer_name=dealer_name,
                price=price, stock=stock, description=description
            )
            medicine.save()
            messages.success(request, "You have added a new medicine.")
            return redirect("customer:view-medicines")
        return redirect("customer:add-medicine")

    context = {
        "form": form
    }
    return render(request, "store/customer/add-medicine.html", context)


@login_required(login_url="/login/customer/")
def update_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    form = UpdateMedicineForm(instance=medicine)

    if request.method == "POST":
        form = UpdateMedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that medicine.")
            return redirect("customer:view-medicines")
        return redirect("customer:update-medicine")

    context = {
        "form": form,
    }
    return render(request, "store/customer/update-medicine.html", context)


@login_required(login_url="/login/customer/")
def delete_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    medicine.delete()
    messages.success(request, "You have successfully deleted that medicine.")
    return redirect("customer:view-medicines")

"""
Medicine CRUD Ends Here
"""

"""
Purchase CRUD Starts Here
"""
@login_required(login_url="/login/customer/")
def purchases_page(request):
    purchases = Purchase.objects.filter(customer=request.user)

    context = {
        "purchases": purchases
    }
    return render(request, "store/customer/view-purchases.html", context)


@login_required(login_url="/login/customer/")
def add_purchase_page(request):
    form = AddPurchaseForm()

    if request.method == "POST":
        form = AddPurchaseForm(request.POST)

        if form.is_valid():
            med_name = form.cleaned_data.get("med_name")
            customer = form.cleaned_data.get("customer")
            price_number = form.cleaned_data.get("price_number")
            quantity = form.cleaned_data.get("quantity")

            purchase = Purchase(
                med_name=med_name, customer=customer,
                price_number=price_number, quantity=quantity
            )
            purchase.save()
            messages.success(request, "You have a new purchase.")
            return redirect("customer:view-purchases")
        return redirect("customer:add-purchase")

    context = {
        "form": form
    }
    return render(request, "store/customer/add-purchase.html", context)


@login_required(login_url="/login/customer/")
def update_purchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    form = UpdatePurchaseForm(instance=purchase)

    if request.method == "POST":
        form = UpdatePurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that purchase.")
            return redirect("customer:view-purchases")
        return redirect("customer:update-purchase")

    context = {
        "form": form,
    }
    return render(request, "store/customer/update-purchase.html", context)


@login_required(login_url="/login/customer")
def delete_purchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    purchase.delete()
    messages.success(request, "You have successfully deleted that purchase.")
    return redirect("customer:view-purchases")

"""
Purchase CRUD Ends Here
"""