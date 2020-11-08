from django.db import models
from datetime import date

class Staff(models.Model):
    name = models.CharField(max_length=64, default='no-name')
    surname = models.CharField(max_length=64, default='no-surname')
    sl_position = models.ManyToManyField("StaffListPosition", blank=True)
    salary = models.DecimalField(max_digits=9, decimal_places=2, default=150_000.00)
    direct = models.ManyToManyField("Direction", blank=True)
    serts = models.ManyToManyField("Sertificate", blank=True)
    # hired = models.DateField(null=True, blank=True)
    # fired = models.DateField(blank=True)
    is_staff = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} {self.surname} (id# {self.id} is staff: {self.is_staff})"
    
class StaffListPosition(models.Model):
    name = models.CharField(max_length=128, default='no-position')
    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(max_length=64, default='no-direction')
    def __str__(self):
        return self.name
    
class Sertificate(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    # start = models.DateField(null=True, blank=True)
    # finish = models.DateField(null=True, blank=True)
    # is_completed = models.BooleanField(default=False)
    # stages = models.ForeignKey("Stage", on_delete=models.SET_NULL, null=True)
    # expenditures = models.DecimalField(max_digits=11, decimal_places=2, default=1.00)
    # team = models.ManyToManyField("Role", blank=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    start_plan = models.DateField(null=True, blank=True)
    start_fact = models.DateField(null=True, blank=True)
    end_plan = models.DateField(null=True, blank=True)
    end_fact = models.DateField(null=True, blank=True)
    exp_plan = models.DecimalField(max_digits=11, decimal_places=2, default=1.00)
    exp_fact = models.DecimalField(max_digits=11, decimal_places=2, default=1.00)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} of {self.proj}"
    
class Role(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)
    stages = models.ManyToManyField(Stage, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.name} in {self.proj}"

