from .models import Task
from django import forms
class ToDoform(forms.ModelForm):
     class Meta:
           model=Task
           fields=['name','priority','time']
