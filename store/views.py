from django.shortcuts import render, redirect
from .forms import CreateUserForm, LogUserForm, AddDealerForm,\
    AddMedicineForm, AddEmployeeForm, AddCustomerForm, AddPurchaseForm,\
        UpdateProfileForm, UpdateUserForm, UpdateDealerForm,\
            UpdateMedicineForm, UpdateEmployeeForm, UpdateCustomerForm,\
                UpdatePurchaseForm, AddOrderForm, UpdateOrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import (
    Dealer, Medicine, Employee,
    Customer, Purchase, Profile
)
from customer.models import Order
from django.contrib.auth.forms import UserCreationForm,\
    AuthenticationForm


def home_page(request):
    return render(request, "store/home.html")


def logout_page(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("store:home")


def login_page(request):
    return render(request, "store/login.html")


def login_admin(request):
    form = LogUserForm()

    if request.method == "POST":
        form = LogUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(
                request, username=username, password=password
            )
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username}, you are logged in.")
                return redirect("store:dashboard-admin")
            messages.error(request, f"Oops, the username {username} does not exist in our database. Please try again.")
        return redirect("store:login-admin")

    context = {
        'form': form
    }
    return render(request, "store/login-admin.html", context)


def login_customer(request):
    form = LogUserForm()

    if request.method == "POST":
        form = LogUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(
                request, username=username, password=password
            )
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username}, you are logged in.")
                return redirect("store:dashboard-customer")
            messages.error(request, f"Oops, the username {username} does not exist in our database. Please try again.")
        return redirect("store:login-customer")

    context = {
        'form': form
    }
    return render(request, "store/login-customer.html", context)


def register_page(request):
    return render(request, "store/register.html")


def register_admin(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has successfully been created.")
            return redirect("store:login")
        print("Something's not right.")
        return redirect("store:register-admin")

    context = {
        'form': form
    }

    return render(request, "store/register-admin.html", context)


def register_customer(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has successfully been created.")
            return redirect("store:login-customer")
        print("Something's not right.")
        return redirect("store:register-customer")

    context = {
        'form': form
    }
    return render(request, "store/register-customer.html", context)


@login_required(login_url="/login/admin/")
def dashboard_admin(request):
    return render(request, "store/dashboard-admin.html")


@login_required(login_url="/login/customer/")
def dashboard_customer(request):
    return render(request, "store/dashboard-customer.html")

"""
Dealers CRUD Starts Here
"""
@login_required(login_url="/login/")
def dealers_page(request):
    dealers = Dealer.objects.all()

    context = {
        'dealers': dealers
    }
    return render(request, "store/view-dealers.html", context)


@login_required(login_url="/login/")
def add_dealer_page(request):
    form = AddDealerForm()

    if request.method == "POST":
        form = AddDealerForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get("fname")
            lname = form.cleaned_data.get("lname")
            address = form.cleaned_data.get("address")
            phone_number = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")
            print(fname, lname)

            dealer = Dealer(
                fname=fname, lname=lname, address=address,
                phone_number=phone_number, email=email
            )
            dealer.save()
            messages.success(request, "You have added a new dealer.")
            return redirect("store:view-dealers")
        return redirect("store:add-dealer")

    context = {
        'form': form
    }
    return render(request, "store/add-dealer.html", context)


@login_required(login_url="/login/")
def update_dealer(request, pk):
    dealer = Dealer.objects.get(id=pk)
    form = UpdateDealerForm(instance=dealer)

    if request.method == "POST":
        form = UpdateDealerForm(request.POST, instance=dealer)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that dealer.")
            return redirect("store:view-dealers")
        return redirect("store:update-dealer")

    context = {
        "form": form,
    }
    return render(request, "store/update-dealer.html", context)


@login_required(login_url="/login/")
def delete_dealer(request, pk):
    dealer = Dealer.objects.get(id=pk)
    dealer.delete()
    messages.success(request, "You have successfully deleted that dealer.")
    return redirect("store:view-dealers")

"""
Dealers CRUD Ends Here
"""

"""
Medicine CRUD Starts Here
"""
@login_required(login_url="/login/")
def medicines_page(request):
    medicines = Medicine.objects.all()

    context = {
        "medicines": medicines
    }
    return render(request, "store/view-medicines.html", context)


@login_required(login_url="/login/")
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
            return redirect("store:view-medicines")
        return redirect("store:add-medicine")

    context = {
        "form": form
    }
    return render(request, "store/add-medicine.html", context)


@login_required(login_url="/login/")
def update_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    form = UpdateMedicineForm(instance=medicine)

    if request.method == "POST":
        form = UpdateMedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that medicine.")
            return redirect("store:view-medicines")
        return redirect("store:update-medicine")

    context = {
        "form": form,
    }
    return render(request, "store/update-medicine.html", context)


@login_required(login_url="/login/")
def delete_medicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    medicine.delete()
    messages.success(request, "You have successfully deleted that medicine.")
    return redirect("store:view-medicines")

"""
Medicine CRUD Ends Here
"""

"""
Employees CRUD Starts Here
"""
@login_required(login_url="/login/")
def employees_page(request):
    employees = Employee.objects.all()

    context = {
        "employees": employees
    }
    return render(request, "store/view-employees.html", context)


@login_required(login_url="/login/")
def add_employee_page(request):
    form = AddEmployeeForm()

    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            """
            imports random function to randomly create a unique emp_id
            """
            import random

            emp_id = random.randrange(000, 999)
            fname = form.cleaned_data.get("fname")
            lname = form.cleaned_data.get("lname")
            address = form.cleaned_data.get("address")
            salary = form.cleaned_data.get("salary")
            phone_number = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")

            employee = Employee(
                emp_id=emp_id, fname=fname, lname=lname, address=address,
                salary=salary, phone_number=phone_number, email=email
            )
            employee.save()
            messages.success(request, "You have added a new employee.")
            return redirect("store:view-employees")
        return redirect("store:add-employee")

    context = {
        "form": form
    }
    return render(request, "store/add-employee.html", context)


@login_required(login_url="/login/")
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = UpdateEmployeeForm(instance=employee)

    if request.method == "POST":
        form = UpdateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that employee.")
            return redirect("store:view-employees")
        return redirect("store:update-employee")

    context = {
        "form": form,
    }
    return render(request, "store/update-employee.html", context)


@login_required(login_url="/login/")
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    messages.success(request, "You have successfully deleted that employee.")
    return redirect("store:view-employees")

"""
Employee CRUD Ends Here
"""

"""
Customer CRUD Starts Here
"""
@login_required(login_url="/login/")
def customers_page(request):
    customers = Customer.objects.all()

    context = {
        "customers": customers
    }
    return render(request, "store/view-customers.html", context)


@login_required(login_url="/login/")
def add_customer_page(request):
    form = AddCustomerForm()

    if request.method == "POST":
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            fname = form.cleaned_data.get("fname")
            lname = form.cleaned_data.get("lname")
            address = form.cleaned_data.get("address")
            phone_number = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")

            customer = Customer(
                fname=fname, lname=lname, address=address,
                phone_number=phone_number, email=email
            )
            customer.save()
            messages.success(request, "You have added a new employee.")
            return redirect("store:view-customers")
        return redirect("store:add-customer")

    context = {
        "form": form
    }
    return render(request, "store/add-customer.html", context)


@login_required(login_url="/login/")
def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = UpdateCustomerForm(instance=customer)

    if request.method == "POST":
        form = UpdateCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that customer.")
            return redirect("store:view-customers")
        return redirect("store:update-customer")

    context = {
        "form": form,
    }
    return render(request, "store/update-customer.html", context)


@login_required(login_url="/login/")
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    messages.success(request, "You have successfully deleted that customer.")
    return redirect("store:view-customers")

"""
Customer CRUD Ends Here
"""

"""
Purchase CRUD Starts Here
"""
@login_required(login_url="/login/")
def purchases_page(request):
    purchases = Purchase.objects.all()

    context = {
        "purchases": purchases
    }
    return render(request, "store/view-purchases.html", context)


@login_required(login_url="/login/")
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
            return redirect("store:view-purchases")
        return redirect("store:add-purchase")

    context = {
        "form": form
    }
    return render(request, "store/add-purchase.html", context)


@login_required(login_url="/login/")
def update_purchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    form = UpdatePurchaseForm(instance=purchase)

    if request.method == "POST":
        form = UpdatePurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully update that purchase.")
            return redirect("store:view-purchases")
        return redirect("store:update-purchase")

    context = {
        "form": form,
    }
    return render(request, "store/update-purchase.html", context)


@login_required(login_url="/login/")
def delete_purchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    purchase.delete()
    messages.success(request, "You have successfully deleted that purchase.")
    return redirect("store:view-purchases")


"""
Purchase CRUD Ends Here
"""

@login_required(login_url="/login/")
def confirm_logout_page(request):
    return render(request, "store/confirm-logout.html")


@login_required(login_url="/login/")
def settings_page(request):
    u_form = UpdateUserForm(instance=request.user)
    p_form = UpdateProfileForm(instance=request.user.profile)

    if request.method == "POST":
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UpdateUserForm(instance=request.user, data=request.POST)

        if p_form.is_valid() and u_form.is_valid():
            username = u_form.cleaned_data.get("username")
            p_form.user = username
            p_form.save()
            messages.success(request, f"{username}, you profile has successfully been updated.")
            return redirect("store:dashboard")
        return redirect("store:settings")

    context = {
        "p_form": p_form,
        "u_form": u_form
    }
    return render(request, "store/settings.html", context)