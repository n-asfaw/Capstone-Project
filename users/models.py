# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_set',  # Add a custom related_name here
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_permission_user_set',  # Add a custom related_name here
#         blank=True
#     )

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_of_membership = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
