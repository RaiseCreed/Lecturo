from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import widgets
from django.forms.utils import ErrorList
from .models import Group, Student, Subject, ScheduledLecture


class GroupForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(GroupForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Group
        fields = ['group_number','full_name']


class StudentForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Student
        fields = ['first_name','last_name']


class StudentEditForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(StudentEditForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Student
        fields = ['first_name','last_name','group']


class SubjectForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(SubjectForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Subject
        fields = ['name']


class LectureForm(ModelForm):

    def __init__(self,*args,**kwargs):
        super(LectureForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = ScheduledLecture
        fields = ['lecture','group','type','description','dateStart','dateEnd']
        labels = {
            'dateStart':'Start',
            'dateEnd':'End',
        }
        widgets = {
            'dateStart': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dateEnd': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }