from django.db import models

# Create your models here.
class zuridashboard(models.Model):
    user = models.CharField(max_length=40)
    studentId = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.user

class tracks(models.Model):
    fulltime = models.CharField(max_length=40)
    parttime = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.fulltime



