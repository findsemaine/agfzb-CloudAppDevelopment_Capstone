from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.name

class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    car_types = [
        (SEDAN, "Sedan"), 
        (SUV, "SUV"), 
        (WAGON, "WAGON")
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.TextField()
    dealer_id = models.IntegerField()
    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=car_types,
        default=SEDAN
    )
    year = models.DateField()
    def __str__(self):
        return self.car_make.name + "," + self.name + " " + self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
