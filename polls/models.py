from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    average_rating = models.FloatField()
    email = models.EmailField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.id} - {self.name}'


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    description = models.TextField()
    maximum_occupancy = models.IntegerField()
    price = models.DecimalField(max_digits=102, decimal_places=2)
    image = models.TextField()

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.name}'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_people = models.IntegerField()
    total_price = models.DecimalField(max_digits=102, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    title = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.title}'
