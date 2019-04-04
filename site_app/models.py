from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Guest(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    attending = models.BooleanField()
    full_name =str(first_name)+str(last_name)

    Veg = 'V'
    Beef = 'B'
    Chicken = 'C'
    meal_options = (
        (Veg, 'Vegetarian'),
        (Beef, 'Beef'),
        (Chicken, 'Chicken'),
    )
    meal_selection = models.CharField(max_length=1, choices=meal_options)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
        

    def get_absolute_url(self):
        return reverse("site_app:detail", kwargs={"pk": self.pk})
    
