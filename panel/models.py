from django.db import models
import uuid
from django.utils import timezone
import random
from users.models import User


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4,blank=False,null=False,editable=False,primary_key=True)
    group_number = models.CharField(max_length=100,blank=False,null=False)
    full_name = models.CharField(max_length=100,blank=False,null=False)
    total_students = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self) -> str:
        return self.group_number
    
    
    def updateStudentCount(self) -> None:
        students = self.student_set.all()
        self.total_students = students.count()
        self.save()


class Student(models.Model):
    album_number = models.IntegerField(unique=True,blank=False,null=False,editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True,null=False,blank=False)
    first_name = models.CharField(max_length=100,blank=False,null=False)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,null=False,blank=False)
    email = models.EmailField(blank=True,null=False,max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False,blank=False,null=False)
    name = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self) -> str:
        return self.name
    
class ScheduledLecture(models.Model):
    LECTURE_TYPE = (
        ('remote','Remote'),
        ('stationary','Stationary')
    )

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False,blank=False,null=False)
    lecture = models.ForeignKey(Subject,blank=False,null=False,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,blank=False,null=True)
    started = models.BooleanField(default=False)
    type = models.CharField(max_length=100,choices=LECTURE_TYPE)
    description = models.TextField(max_length=300,blank=True,null=True)
    dateStart = models.DateTimeField(blank=False,null=False)
    dateEnd = models.DateTimeField(blank=False,null=False)

    def __str__(self) -> str:
        return f"{self.lecture.name} ({self.group.group_number})"
    
    def isOngoing(self):
        if self.dateStart <= timezone.now():
            self.started = True
        else:
            self.started = False

        self.save()

    class Meta:
        ordering = ['dateStart']


class Attendance(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(ScheduledLecture,on_delete=models.CASCADE)
    present = models.BooleanField(default=None,blank=True,null=True)


    def __str__(self) -> str:
        return f"Attendance {self.lecture.lecture.name} on {self.created}"
    
    class Meta:
        unique_together = ('student', 'lecture')



class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True,blank=False,null=False)
    sender = models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
    recipent = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=False,blank=False)
    body = models.TextField(blank=False,null=False)
    is_read = models.BooleanField(blank=False,null=False,default=False)


    def __str__(self) -> str:
        return self.title
    
    @property
    def setAsRead(self):
        self.is_read = True
        self.save()

    @property
    def setAsUnread(self):
        self.is_read = False
        self.save()


    class Meta:
        ordering = ['is_read']
    