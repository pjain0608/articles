from django.db import models

# Create your models here.
class articles(models.Model):
    Heading = models.CharField(max_length=100)
    Description = models.CharField(max_length=2000)

    def __str__(self):
        return self.Heading