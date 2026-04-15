from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Dealer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fname} {self.lname}" 

    def get_update_url(self):
        return reverse("store:update-dealer", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("store:delete-dealer", kwargs={"pk": self.pk})


class Medicine(models.Model):
    med_code = models.IntegerField()
    med_name = models.CharField(max_length=50)
    dealer_name = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.med_code}: {self.med_name}"

    def get_update_url(self):
        return reverse("store:update-medicine", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("store:delete-medicine", kwargs={"pk": self.pk})


class Employee(models.Model):
    emp_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    salary = models.FloatField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.emp_id}: {self.fname} {self.lname}"

    def get_update_url(self):
        return reverse("store:update-employee", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("store:delete-employee", kwargs={"pk": self.pk})


class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fname} {self.lname}"

    def get_update_url(self):
        return reverse("store:update-customer", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("store:delete-customer", kwargs={"pk": self.pk})


class Purchase(models.Model):
    med_name = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    price_number = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.med_name} {self.customer}"

    def get_update_url(self):
        return reverse("store:update-purchase", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("store:delete-purchase", kwargs={"pk": self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(default="users/me.jpg", upload_to="users/")

    def __str__(self):
        return self.user.username

    # Resize User Profile Picture 
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        profile_picture = Image.open(self.profile_picture.path)
        if profile_picture.height > 300 or profile_picture.width > 300:
            output_size = (300, 300)
            profile_picture.thumbnail(output_size)
        print(profile_picture)
        

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
