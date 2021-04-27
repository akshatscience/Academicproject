from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.



class Voter(models.Model):
    
    voter_id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=45,null=False)
    email = models.EmailField(max_length=300)
    gender = models.CharField(max_length=45,null=False)
    age = models.CharField(max_length=45,null=False)
    city = models.CharField(max_length=45,null=False)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'voter'




class Election(models.Model):
    elction_id=models.AutoField(primary_key=True,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=CASCADE,null=True)
    name=models.CharField(max_length=200)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    reg_start_date=models.DateTimeField(default=datetime.now)
    reg_end_date=models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name


class Candidate(models.Model):
    gen=(('male','male'),
    ('female','female'),
    ('transgender','transgender'))


    Candidate_id=models.AutoField(primary_key=True,unique=True,null=False,blank=True)
    election=models.ForeignKey(Election,on_delete=CASCADE,null=True)
    AADHAR_NO=models.CharField(max_length=16)
    name=models.CharField(max_length=100,null=False,blank=False)
    gender=models.CharField(max_length=20,choices=gen,null=False,blank=False)
    age = models.CharField(max_length=45,null=False,blank=False)
    vote_count=models.IntegerField(default=0)
    Candidate_photo=models.ImageField(upload_to='')
    party_symbol=models.ImageField(upload_to='',null=True)
  
    def __str__(self):
        return self.name

    
    



