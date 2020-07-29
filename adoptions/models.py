from django.db import models

class Pet(models.Model):
	name = models.CharField(max_length=100)
	submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=20)
	submission_date = models.DateTimeField()
	description = models.TextField(blank=True)