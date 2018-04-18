from django.db import models

# Create your models here.
class Team(models.Model):
    name= models.CharField(max_length=200)
    description= models.CharField(max_length=200)
    logo=models.ImageField(upload_to='photos')
    code= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Player(models.Model):
    name= models.CharField(max_length=50)
    nickname= models.CharField(max_length=50)
    birth_date= models.DateField()
    age_old=models.IntegerField()
    rut=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    height=models.IntegerField()
    weight=models.IntegerField()
    photo=models.ImageField(upload_to='photos')

    BASE='BA'
    ESCOLTA='EC'
    ALERO='AL'
    ALA_PIVOT='AP'
    PIVOT='PV'
    POSITION_GAME_CHOICES = (
        (BASE,'Base'),
        (ESCOLTA,'Escolta'),
        (ALERO,'Alero'),
        (ALA_PIVOT,'Ala_Pivot'),
        (PIVOT,'Pivot'),
    )
    positionGame=models.CharField(
        max_length=2,
        choices=POSITION_GAME_CHOICES,
        default=BASE,
    )



    def __str__(self):
        return self.name

class Coach(models.Model):
    name= models.CharField(max_length=50)
    age_old=models.IntegerField()
    email=models.CharField(max_length=50)
    rut=models.CharField(max_length=30)
    nickname= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Match(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
