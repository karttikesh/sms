from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, name, email, mobile, username, password=None):
        if not email:
            raise ValueError("The Email field must be set.")
        
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, mobile=mobile, username=username)
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, email, mobile, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        user = self.model(name=name, email=email, mobile=mobile, username=username)
        user.set_password(password)
        user.is_active = False
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserRole(models.Model):
    role = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} - {self.description}"

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    username = models.CharField(max_length=100, unique=True)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, related_name='UserRole', null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'mobile']

    objects = UserManager()

    def __str__(self):
        return f"{self.name} - {self.username}"
    
    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return super().has_perm(perm, obj)
    
    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return super().has_module_perms(app_label)
