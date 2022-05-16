from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.TextField(max_length=256)

    def __str__(self):
        return f'{self.id} - {self.name}'

class Student(models.Model):
  code = models.TextField(max_length=10)
  name = models.TextField(max_length=256)
  address = models.TextField(max_length=256)
  department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=False,
        null=True)

  def __str__(self):
    return f'{self.id} - {self.code} - {self.name}'