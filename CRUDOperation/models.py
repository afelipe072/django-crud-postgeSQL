from django.db import models

class EmpModel (models.Model):
    empnombre=models.CharField(max_length=20)
    empapellido=models.CharField(max_length=20)
    cargo=models.CharField(max_length=20)
    salario=models.IntegerField()
    genero=models.CharField(max_length=1)
    class Meta:
        db_table="empleado"
