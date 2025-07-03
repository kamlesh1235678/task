from django.db import models

# Create your models here.
class FlightData(models.Model):
    airline = models.CharField(max_length=100)
    source = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    price = models.CharField(max_length=20)
    departure_time = models.CharField(max_length=100)
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.airline}: {self.source} to {self.destination} at {self.price}"