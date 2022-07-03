from django.db import models

# Create your models here.
class student(models.Model):
    slno=models.PositiveIntegerField(primary_key=True)
    nane=models.CharField(max_length=30)
    rollno=models.BigIntegerField()
    phno=models.CharField(max_length=10)
class topic(models.Model):
    topic_name=models.CharField(max_length=20,primary_key=True)
class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,primary_key=True)
    url=models.URLField()
class record(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()