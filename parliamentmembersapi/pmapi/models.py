from django.db import models

# Create your models here.


class ParliamentMember(models.Model):

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    political_force = models.CharField(max_length=100, blank=True, null=True)
    language1 = models.CharField(max_length=100, blank=True, null=True)
    language2 = models.CharField(max_length=100, blank=True, null=True)
    language3 = models.CharField(max_length=100, blank=True, null=True)
    language4 = models.CharField(max_length=100, blank=True, null=True)
    language5 = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    profession1 = models.CharField(max_length=100, blank=True, null=True)
    profession2 = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        pass
