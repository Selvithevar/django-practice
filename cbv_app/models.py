from django.db import models
from django.urls import reverse
# Create your models here.
class students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    testScore = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})