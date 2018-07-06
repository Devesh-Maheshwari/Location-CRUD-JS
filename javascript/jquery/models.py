from django.db import models


class Maps(models.Model):
    address=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    def __str__(self):
        return self.address