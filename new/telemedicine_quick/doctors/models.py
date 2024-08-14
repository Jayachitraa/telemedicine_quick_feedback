from django.db import models

# first_name: CharField
# last_name: CharField
# specialization: CharField
# email: EmailField


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name=  models.CharField(max_length=100)
    specialization =models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

