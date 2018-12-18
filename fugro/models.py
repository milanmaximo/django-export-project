from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.shortcuts import render_to_response
import csv
import xlrd
from django.http import HttpResponse


# from .resources import FurgoResource


class Utilisation(models.Model):
    name = models.CharField(max_length=30, blank=True, )

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=30, blank=True, )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=30, blank=True, default=None)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, blank=True, default=None)

    def __str__(self):
        return self.name


class Fugro(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True, default=None)
    date = models.DateField(null=True)
    worktime = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=50)
    utilisation = models.ForeignKey('Utilisation', on_delete=models.CASCADE, blank=True, default=None)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, blank=True, default=None, )
    car = models.ForeignKey('Car', on_delete=models.CASCADE, blank=True)
    comment = models.TextField(blank='')
    comment_project = models.TextField(blank='')
    comment_equipment = models.TextField(blank='')
    comment_car = models.TextField(blank='')


    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'fugro'
        verbose_name_plural = 'fugros'


