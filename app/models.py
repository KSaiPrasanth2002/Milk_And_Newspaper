from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserRegistration(AbstractUser):
    phoneNumber = models.CharField(_('phone number'), max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'app_userregistration'

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='%(class)s_user_permissions',
        related_query_name='%(class)s_user_permission',
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions'
            'granted to each of their groups.'
        ),
        related_name='%(class)s_user_groups',
        related_query_name='%(class)s_user_group',
    )