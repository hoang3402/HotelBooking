from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)
    currency = models.CharField(max_length=18)

    def __str__(self):
        return self.name


class City(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True)
    phone_number = models.CharField(max_length=20)
    average_rating = models.FloatField(default=0)
    email = models.EmailField()
    image = models.CharField(max_length=255)

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    features = models.ManyToManyField('polls.HotelFeatures', through='polls.SpecificHotelFeature')

    def __str__(self):
        return f'{self.id} - {self.name}'


class RoomType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    adults = models.IntegerField()
    children = models.IntegerField()
    price = models.DecimalField(max_digits=102, decimal_places=2)
    image = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.room_type} - {self.hotel.name}'


# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, number_phone, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            number_phone=number_phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, number_phone, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, number_phone, **extra_fields)

    def create_staff(self, email, password, first_name, last_name, number_phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, number_phone, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, number_phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, number_phone, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    number_phone = models.CharField(max_length=50)

    # is_staff and is_active must be needed, otherwise you won't be able to log in django-admin.
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)  # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'number_phone']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Booking(models.Model):
    type_status = {
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    }

    id = models.AutoField(primary_key=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    total_price = models.DecimalField(max_digits=102, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=type_status, default='Pending')

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    title = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.title}'


class HotelFeatures(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.code} - {self.description}'


class SpecificHotelFeature(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    feature = models.ForeignKey(HotelFeatures, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('hotel', 'feature')
