
from django.db import models



class studentsdata (models.Model):

    name= models.CharField (max_length=40)

    last_name= models.CharField(max_length=40)

    address= models.CharField (max_length=50)
  

class personaldata (models.Model):

    age= models.IntegerField()

    height= models.IntegerField()

    weight= models.IntegerField()

    preexisting_condition= models.CharField (max_length=50)


class additionaldata (models.Model):

    extra_activities= models.CharField (max_length=50)

    training_style= models.CharField (max_length=50)

    proposed_objectives= models.CharField (max_length=50)
    