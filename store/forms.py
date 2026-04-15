from django import forms
from django.contrib.auth.models import User
from .models import Dealer, Medicine, Employee, Customer,\
    Purchase, Profile
from customer.models import Order
from django.contrib.auth.forms import UserCreationForm,\
    AuthenticationForm


class AddDealerForm(forms.ModelForm):
    """"
    This class creates a dealer.
    """
    class Meta:
        model = Dealer
        fields = ['fname', 'lname', 'address', 'phone_number', 'email']
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPhoneNumber',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control user_input',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "email"
                }
            ),
        }


class UpdateDealerForm(forms.ModelForm):
    """"
    This class updates a dealer.
    """
    class Meta:
        model = Dealer
        fields = ['fname', 'lname', 'address', 'phone_number', 'email']
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPhoneNumber',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control user_input',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "email"
                }
            ),
        }


class AddMedicineForm(forms.ModelForm):
    
    class Meta:
        model = Medicine
        fields = [
            "med_code", "med_name", "dealer_name",
            "price", "stock", "description"
        ]
        widgets = {
            'med_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationMedCode',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'med_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'dealer_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'stock': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
        }


class UpdateMedicineForm(forms.ModelForm):
    
    class Meta:
        model = Medicine
        fields = [
            "med_code", "med_name", "dealer_name",
            "price", "stock", "description"
        ]
        widgets = {
            'med_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationMedCode',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'med_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'dealer_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'stock': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
        }


class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            "fname", "lname", "address",
            "salary", "phone_number", "email"
        ]
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': 'email'
                }
            ),
        }


class UpdateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            "fname", "lname", "address",
            "salary", "phone_number", "email"
        ]
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': 'email'
                }
            ),
        }


class AddCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = [
            "fname", "lname", "address",
            "phone_number", "email"
        ]
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': 'email'
                }
            ),
        }


class UpdateCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = [
            "fname", "lname", "address",
            "phone_number", "email"
        ]
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': 'email'
                }
            ),
        }


class AddPurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = [
            "customer", "med_name", "price_number", "quantity"
        ]
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationCustomer',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'med_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
        }

class UpdatePurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase
        fields = [
            "med_name", "customer", "price_number", "quantity"
        ]
        widgets = {
            'med_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationCustomer',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
        }


class AddOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            "customer", "med_name", "price", "quantity"
        ]
        widgets = {
            'med_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationCustomer',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
        }


class UpdateOrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            "customer", "med_name", "price", "quantity"
        ]
        widgets = {
            'med_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationCustomer',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'quantity': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
        }


class CreateUserForm(UserCreationForm):
    """
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given 
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword2',
            'required': 'true',
            }
        ),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        ),
    }


class LogUserForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with no privileges, from the given 
    username and password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        )
    )


class UpdateProfileForm(forms.ModelForm):
    """
    This form updates a user profile, from the given 
    bio and profile_picture fields.
    """
    profile_picture = forms.FileField()
    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'profile_picture']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
    }


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "username", "email"
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
            'id': 'inputFirstName3MD',
        }),
        'last_name': forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control',
            'id': 'inputLastName3MD',
        }),
        'username': forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
            'id': 'inputUserName3MD',
        }),
        'email': forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
            'id': 'inputEName3MD',
        }),
    }