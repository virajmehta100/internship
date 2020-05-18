from django.db import models

class veg(models.Model):
    recipe = models.CharField(max_length=1000)
    minerals = models.CharField(max_length=500)
    vitamins = models.CharField(max_length=500)
    recipe_photo = models.CharField(max_length=1000)

    def __str__(self):
        return self.recipe + '-' + self.minerals


class veg_people(models.Model):
    Veg = models.ForeignKey(veg, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    name_of_people = models.CharField(max_length=500)



