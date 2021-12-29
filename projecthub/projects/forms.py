from django.forms import ModelForm
from .models import Project

class ProjectsForm(ModelForm):
    class Meta:
        model = Project
         # exclude = ['project_priority_sl']
        fields = '__all__'