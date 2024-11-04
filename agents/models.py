# models.py

from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubCounty(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Parish(models.Model):
    name = models.CharField(max_length=100)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Village(models.Model):
    name = models.CharField(max_length=100)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PollingStation(models.Model):
    name = models.CharField(max_length=100)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Agent(models.Model):
    agent_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
