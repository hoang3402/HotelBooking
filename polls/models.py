from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    average_rating = models.FloatField(default=0)
    email = models.EmailField()
    image = models.CharField(max_length=255)

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
    maximum_occupancy = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=102, decimal_places=2)
    image = models.CharField(max_length=255)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.room_type} - {self.hotel.name}'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.id} - {self.name}'


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
    number_of_people = models.IntegerField()
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
