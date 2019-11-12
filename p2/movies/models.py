from django.db import models

# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length = 120, null=False)
    lname = models.CharField(max_length = 120, null=False)

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)



class Movie(models.Model):
    titile = models.CharField(max_length = 120, null=False)
    director = models.ForeignKey(Person, on_delete=models.PROTECT, null=False)
    release = models.DateField()

    def __str__(self):
        return self.titile