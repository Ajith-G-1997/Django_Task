from django.db import models
from django.db.models import CharField,EmailField,IntegerField,ForeignKey,ImageField,TextField,ImageField,FileField

class CLASS_CHOICES(models.Model):
    name=CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    admission_no =CharField(max_length=10, unique=True)
    full_name = CharField(max_length=50)
    email =EmailField(max_length=100)
    age = IntegerField()
    class_level = ForeignKey(CLASS_CHOICES, on_delete=models.CASCADE)
    description = TextField()
    image = ImageField(upload_to='static/img')
    marklist = FileField(upload_to='static/marklists/')

    def __str__(self):
        return self.full_name



