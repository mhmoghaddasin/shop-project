from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    mobile = models.CharField(_('mobile_number'), max_length=14, db_index=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='user/image/', null=True, blank=True, default='')

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.last_name + " " + self.first_name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(_('City'), max_length=50)
    street = models.CharField(_('street'), max_length=100)
    alley = models.CharField(_('alley'), max_length=100)
    zip_code = models.CharField(_('zip code'), max_length=10)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return '{} address'. format(self.user)

class UserEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Subject = models.CharField(_('Subject'), max_length=150)
    body = models.TextField(_('body'),)

    class Meta:
        verbose_name = _('UserEmail')
        verbose_name_plural = _('UserEmails')

    def __str__(self):
        return self.user, "email"

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=150)
    description = models.CharField(_('description'), max_length=256)
    slug = models.SlugField(_('slug'), )
    image = models.ImageField(verbose_name=_('image'), upload_to='shop/image/', null=True, blank=True)

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

    def __str__(self):
        return self.name
