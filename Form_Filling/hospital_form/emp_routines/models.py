
from django.db import models
from users.models import User

# Create your models here.


class EmpRoutines(models.Model):
    REPEAT_CHOICES = (
        ('None', 'None'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly')
    )
    SHIFT_CHOICES = (
        ('Morning Shift - 5am to 9am', 'Morning Shift - 5am to 9am'),
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    repeat = models.CharField(max_length=15, choices=REPEAT_CHOICES)
    shift_availablity = models.CharField(max_length=35, choices=SHIFT_CHOICES)
    weekdays = models.CharField(max_length=200)

    def __str__(self):
        return self.client.email
