from django.db import models
from django.forms import ModelForm
from django.core import validators
import re


def validate_even(value):
    if re.match('^[a-z]+[0-9]*@gmail.com$',value) == None:
        raise validators.ValidationError('inter a valid email')



class Author(models.Model):
    even_field = models.CharField(validators=[validate_even],max_length=200)

    def __str__(self):
        return self.even_field



class myform(ModelForm):
    class Meta:
        model=Author
        fields=['even_field']
