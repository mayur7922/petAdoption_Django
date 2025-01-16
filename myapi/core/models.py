from django.db import models #type: ignore

class Pet(models.Model):
    type = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    isAdopted = models.BooleanField(default=False)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.type} - {self.breed}"