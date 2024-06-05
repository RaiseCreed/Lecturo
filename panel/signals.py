from django.db.models.signals import post_save, pre_save
from .models import Student, Group



def increaseCounter(sender,instance: Student,created,**kwargs):
    if created:
        group: Group = instance.group
        group.updateStudentCount()

def createEmail(sender,instance: Student,**kwargs):
    instance.email = f"{instance.first_name}.{instance.last_name}@lecturo.edu".lower()


post_save.connect(increaseCounter,sender=Student)
pre_save.connect(createEmail,sender=Student)