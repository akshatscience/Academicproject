from django.db.models.base import Model
from .models import Candidate, Election, Voter
from django import forms

from django.db import models


class CandidateRegistrationform(forms.ModelForm):
    class Meta:
        model=Candidate
        exclude=['vote_count']

class ElectionForm(forms.ModelForm):
    start_date=forms.DateTimeField()
    end_date=forms.DateTimeField()
    class Meta:
        model=Election
        exclude=['user']

class Voters(forms.Form):
    
    user_id=forms.CharField(max_length=16)
    OTP=forms.CharField(max_length=4)


# class AdminForm(forms.ModelForm):
#     password = forms.CharField(max_length=20,widget=forms.PasswordInput)
#     class Meta:
#         model =Admin
#         fields ='__all__'

# class AdminLogin(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=20,widget=forms.PasswordInput)
