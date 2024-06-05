from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    # Groups
    path('groups/',views.listGroups,name='groups'),
    path('groups/<str:pk>/',views.listSingleGroup,name='group'),
    path('add-group/',views.createGroup,name='createGroup'),
    path('edit-group/<str:pk>/',views.editGroup,name='editGroup'),
    path('delete-group/<str:pk>/',views.deleteGroup,name='deleteGroup'),

    # Students
    path('add-student/<str:pk>/',views.createStudent,name='createStudent'),
    path('edit-student/<str:pk>/',views.editStudent,name='editStudent'),
    path('delete-student/<str:pk>/',views.changeActiveStatus,name='changeActiveStatus'),
    path('student/<str:pk>/',views.showStudent,name='showStudent'),

    # Subjects
    path('subjects/',views.subjects,name='subjects'),
    path('add-subjects/',views.createSubject,name='createSubject'),
    path('edit-subjects/<str:pk>/',views.editSubject,name='editSubject'),
    path('delete-subjects/<str:pk>/',views.deleteSubject,name='deleteSubject'),

    # Schedule
    path('schedule/',views.showSchedule,name='schedule'),
    path('add-lecture/',views.createLecture,name='createLecture'),
    path('delete-lecture/<str:pk>/',views.deleteLecture,name='deleteLecture'),
    path('edit-lecture/<str:pk>/',views.editLecture,name='editLecture'),

    # Attendance
    path('edit-attendance/<str:pk>/',views.editAttendance,name='editAttendance'),

    # Messages
    path('messages/',views.messages,name='messages'),
    path('messages/<str:pk>/',views.showMessage,name='showMessage'),
    path('setUnread/<str:pk>/',views.setUnread,name='setUnread'),

    # Profile
    path('profile/',views.profile,name='profile')
]