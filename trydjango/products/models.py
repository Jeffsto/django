from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=65)
    summary     = models.TextField()
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        #return f"/products/{self.id}/"
        return reverse("product", kwargs={"my_id": self.id})