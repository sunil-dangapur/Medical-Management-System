from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from store.models import Medicine
from PIL import Image


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    med_name = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.customer}: {self.med_name}"

    def get_update_url(self):
        return reverse("customer:update-order", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("customer:delete-order", kwargs={"pk": self.pk})


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Customer Profile")
#     phone_number = models.CharField(max_length=20)
#     profile_picture = models.ImageField(default="users/me.jpg", upload_to="users/")

#     def __str__(self):
#         return self.user.username

#     # Resize User Profile Picture 
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         super().save()
#         profile_picture = Image.open(self.profile_picture.path)
#         if profile_picture.height > 300 or profile_picture.width > 300:
#             output_size = (300, 300)
#             profile_picture.thumbnail(output_size)
#         print(profile_picture)
        

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
