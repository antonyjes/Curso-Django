from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, verbose_name='Dni', unique=True)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']

class EmployeeCat(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.employee

    class Meta:
        verbose_name = 'EmpleadoCateg'
        verbose_name_plural = 'EmpleadosCategs'
        db_table = 'empleadocat'
        ordering = ['id']