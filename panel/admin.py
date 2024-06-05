from django.contrib import admin
from .models import Student, Group, Subject, ScheduledLecture, Attendance, Message


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(ScheduledLecture)
admin.site.register(Attendance)
admin.site.register(Message)

# Register your models here.
