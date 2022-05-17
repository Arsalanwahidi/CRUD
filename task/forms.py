from cProfile import label
from pyexpat import model
from attr import attr, attrs, field
from django import forms
from task.models import ModelTask

#Create Your Form Here

class FormTask(forms.ModelForm):

    class Meta:
        model = ModelTask
        fields = ['title_task', 'description_task', 'start_date', 'end_date']
