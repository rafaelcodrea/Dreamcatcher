from django.db import models

class Dream(models.Model):
    description = models.CharField(max_length = 255)
    duration = models.BigIntegerField()
    stress_level = models.BigIntegerField()
    energy = models.BigIntegerField()
