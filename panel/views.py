from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Group, Student, Subject, ScheduledLecture, Attendance, Message
from .forms import GroupForm, StudentForm, StudentEditForm,SubjectForm, LectureForm
import random
import datetime
from django.utils import timezone

@login_required(login_url='userLogin')
def home(request):
    label = "Dashboard"

    newMessages = Message.objects.filter(is_read__exact=False).count()
    closestEvent = ScheduledLecture.objects.filter(

        # First we check if there is ongoing lecture
        (
        Q(dateStart__lte=timezone.now()) &
        Q(dateEnd__gte=timezone.now())
        ) | # If there is no ongoing lecture, we will search for the closest one
        Q(dateStart__gte=timezone.now())
        
    ).order_by('dateStart')
    
    event = closestEvent[0] if closestEvent.count() > 0 else None


    context = {'label':label,'newMessages':newMessages,'quote':'Things start out as hopes and end up as habits.','quoteAuthor':'Lillian Hellman','event':event}
    return render(request,'home.html',context=context)


# Groups
@login_required(login_url='userLogin')
def listGroups(request):
    label = "Groups"
    groups = Group.objects.all()

    context = {'groups':groups,'label':label}
    return render(request,'groups.html',context=context)


@login_required(login_url='userLogin')
def listSingleGroup(request,pk):
    group = Group.objects.get(id=pk)
    students = group.student_set.all()
    label = f"Group details: {group}"

    context = {'group':group,'students':students,'label':label}
    return render(request,'single-group.html',context=context)

@login_required(login_url='userLogin')
def createGroup(request):
    label = "Create group"

    form = GroupForm()
    context = {'form':form,'label':label,'objectName':'group'}

    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('groups')
        else:
            context.update({'error':form.errors.as_text})


    return render(request,'create-object.html',context=context)


@login_required(login_url='userLogin')
def editGroup(request,pk):
    label = "Edit group"

    context = {'label':label,'objectName':'group'}

    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return render(request,'notFound.html')
    
    form = GroupForm(instance=group)

    if request.method == 'POST':
        form = GroupForm(request.POST,instance=group)

        if form.is_valid():
            form.save()

            return redirect('groups')
        else:
            context.update({'error':form.errors.as_text})

    context.update({'form':form})
    return render(request,'edit-object.html',context=context)


@login_required(login_url='userLogin')
def deleteGroup(request,pk):
    label = "Delete group"

    operation = "delete"

    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return render(request,'notFound.html')
    
    if request.method == 'POST':
        group.delete()
        return redirect('groups')
    
    context = {'object':group,'operation':operation,'label':label}
    return render(request,'delete-object.html',context=context)


# Students

@login_required(login_url='login')
def showStudent(request,pk):
    label = "Student details"

    try:
        student = Student.objects.get(album_number=pk)
    except Student.DoesNotExist:
        return render(request,'notFound.html')
    
    attendancePercentage = []

    for subject in Subject.objects.distinct().all():
        presence = Attendance.objects.filter(Q(lecture__lecture__name=subject.name) & Q(student__exact = student)).exclude(present__exact=None)
        if presence.count() == 0:
            continue
        else:
            present = Attendance.objects.filter(Q(lecture__lecture__name=subject.name) & Q(student__exact = student) & Q(present__exact=True))
            percentage = round((present.count()/presence.count()) * 100,1)

            attendancePercentage.append((subject.name, percentage))

    context = {'student':student,'attendancePercentage':attendancePercentage,'label':label}
    return render(request,'student.html',context=context)


@login_required(login_url='userLogin')
def createStudent(request, pk):
    label = "Create student"

    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return render(request,'notFound.html')
        
    form = StudentForm()
    context = {'form':form,'label':label,'objectName':'student'}

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.album_number = random.randint(111111,999999)
            student.group = group
            student.save()

            return redirect('group',pk)
        else:
            context.update({'error':form.errors.as_text})

    return render(request,'create-object.html',context=context)


@login_required(login_url='userLogin')
def editStudent(request,pk):
    label = "Edit student"


    context = {'label':label,'objectName':'student'}

    try:
        student = Student.objects.get(album_number=pk)
    except Student.DoesNotExist:
        return render(request,'notFound.html')
    
    form = StudentEditForm(instance=student)

    if request.method == 'POST':
        form = StudentEditForm(request.POST,instance=student)

        if form.is_valid():
            student = form.save()

            group = student.group
            return redirect('group',group.id)
        else:
            context.update({'error':form.errors.as_text})

    context.update({'form':form})
    return render(request,'edit-object.html',context=context)


@login_required(login_url='userLogin')
def changeActiveStatus(request,pk):
    label = "Change status"

    try:
        student = Student.objects.get(album_number=pk)
    except Student.DoesNotExist:
        return render(request,'notFound.html')
    
    operation = "deactivate" if student.active == True else "activate"

    if request.method == 'POST':

        if operation == "deactivate":
            student.active = False
        else:
            student.active = True

        group = student.group
        student.save()

        return redirect('group',group.id)
    
    context = {'object':student,'operation':operation,'label':label}
    return render(request,'delete-object.html',context=context)


# Subjects
@login_required(login_url='userLogin')
def subjects(request):
    label = "Subjects"

    subjects = Subject.objects.all()

    context = {'subjects':subjects,'label':label}
    return render(request,'subjects.html',context=context)



@login_required(login_url='userLogin')
def createSubject(request):
    label = "Create subject"

    form = SubjectForm()
    context = {'form':form,'label':label,'objectName':'subject'}

    if request.method == 'POST':

        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('subjects')
        else:
            context.update({'error':form.errors.as_text})

    return render(request,'create-object.html',context=context)


@login_required(login_url='userLogin')
def editSubject(request,pk):
    label = "Edit subject"


    context = {'label':label,'objectName':'subject'}

    try:
        subject = Subject.objects.get(id=pk)
    except Subject.DoesNotExist:
        return render(request,'notFound.html')
    
    form = SubjectForm(instance=subject)

    if request.method == 'POST':
        form = SubjectForm(request.POST,instance=subject)

        if form.is_valid():
            subject = form.save()

            return redirect('subjects')
        else:
            context.update({'error':form.errors.as_text})

    context.update({'form':form})
    return render(request,'edit-object.html',context=context)


@login_required(login_url='userLogin')
def deleteSubject(request,pk):
    label = "Delete subject"


    operation = "delete"
    
    try:
        subject = Subject.objects.get(id=pk)
    except Subject.DoesNotExist:
        return render(request,'notFound.html')
    

    if request.method == 'POST':
        subject.delete()

        return redirect('subjects')
    
    context = {'object':subject,'operation':operation,'label':label}
    return render(request,'delete-object.html',context=context)


@login_required(login_url='userLogin')
def showSchedule(request):
    label = "Schedule"

    date = request.GET.get('day')

    if date:
        try:
            dateObject = datetime.datetime.strptime(date,'%Y-%m-%d')
        except ValueError:
            dateObject = datetime.date.today()
    else:
        dateObject = datetime.date.today()

    date = dateObject.strftime('%B %d, %Y')

    next_date = dateObject + datetime.timedelta(days=1)
    prev_date = dateObject - datetime.timedelta(days=1)

    lectures = ScheduledLecture.objects.filter(dateStart__icontains=dateObject.strftime('%Y-%m-%d'))

    for lecture in lectures:
        lecture.isOngoing()

    context = {'lectures':lectures,'date':date,'next_date':next_date.strftime('%Y-%m-%d'),'prev_date':prev_date.strftime('%Y-%m-%d'),'label':label}
    return render(request,'schedule.html',context=context)


@login_required(login_url='userLogin')
def createLecture(request):
    label = "Create lecture"

    form = LectureForm()
    context = {'form':form,'label':label,'objectName':'lecture'}

    if request.method == 'POST':

        form = LectureForm(request.POST)

        if form.is_valid():
            lecture: ScheduledLecture = form.save(commit=False)

            overlappingLectures = ScheduledLecture.objects.filter(Q(dateEnd__gt=lecture.dateStart) & Q(dateStart__lt=lecture.dateEnd)).exclude(id__exact=lecture.id)

            if lecture.dateStart >= lecture.dateEnd:
                # Check if endDate is before startDate
                context.update({'error':'"Start date" have to be before "End date"'})
            elif len(overlappingLectures): 
                # Check if there are any lectures that are overlapping
                context.update({'error':'This lecture cannot be added because its duration overlaps with another lecture!'})
            else:
                lecture.save()
                return redirect('schedule')
        else:
            context.update({'error':form.errors.as_text})

    return render(request,'create-object.html',context=context)


@login_required(login_url='userLogin')
def editLecture(request,pk):
    label = "Edit lecture"


    context = {'label':label,'objectName':'lecture'}

    try:
        lecture = ScheduledLecture.objects.get(id=pk)
    except ScheduledLecture.DoesNotExist:
        return render(request,'notFound.html')
    
    form = LectureForm(instance=lecture)

    if request.method == 'POST':
        form = LectureForm(request.POST,instance=lecture)

        if form.is_valid():
            lecture = form.save(commit=False)

            overlappingLectures = ScheduledLecture.objects.filter(Q(dateEnd__gt=lecture.dateStart) & Q(dateStart__lt=lecture.dateEnd)).exclude(id__exact=lecture.id)

            if lecture.dateStart >= lecture.dateEnd:
                # Check if endDate is before startDate
                context.update({'error':'"Start date" have to be before "End date"'})
            elif len(overlappingLectures): 
                # Check if there are any lectures that are overlapping
                context.update({'error':'This lecture cannot be modified because its duration overlaps with another lecture!'})
            else:
                lecture.save()
                return redirect('schedule')
        else:
            context.update({'error':form.errors.as_text})

    context.update({'form':form})
    return render(request,'edit-object.html',context=context)



@login_required(login_url='userLogin')
def deleteLecture(request,pk):
    label = "Delete lecture"


    operation = "delete"
    
    try:
        lecture = ScheduledLecture.objects.get(id=pk)
    except ScheduledLecture.DoesNotExist:
        return render(request,'notFound.html')
    

    if request.method == 'POST':
        lecture.delete()

        return redirect('schedule')
    
    context = {'object':lecture,'operation':operation,'label':label}
    return render(request,'delete-object.html',context=context)



@login_required(login_url='userLogin')
def editAttendance(request,pk):
    label = "Edit attendance"

    try:
        lecture = ScheduledLecture.objects.get(id=pk)
    except ScheduledLecture.DoesNotExist:
        return render(request,'notFound.html')

    group = lecture.group
    
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken':
                continue
            
            album_number = key.split('-')[1]

            try:
                student = Student.objects.get(album_number=album_number)
            except Student.DoesNotExist:
                return render(request,'notFound.html')
            

            obj, created = Attendance.objects.get_or_create(
                student = student,
                lecture = lecture
            )

            obj.present = True if value == 'present' else False
            obj.save()

    attendanceTuple = []

    for student in group.student_set.exclude(active__exact=False):

        try:
            attendance = Attendance.objects.get(Q(lecture__exact=lecture) & Q(student__exact=student))
            attendance = attendance.present
        except Attendance.DoesNotExist:
            attendance = None
        
        attendanceTuple.append((student,attendance))

    context = {'attendanceTuple':attendanceTuple,'label':label}
    return render(request,'edit-attendance.html',context=context)


@login_required(login_url='login')
def messages(request):
    label = "Messages"

    messages = Message.objects.all()

    context = {'label':label,'messages':messages}
    return render(request,'messages.html',context = context)


@login_required(login_url='login')
def showMessage(request,pk):
    label = "Message details"

    try:
        message = Message.objects.get(id=pk)
    except Message.DoesNotExist:
        return render(request,'notFound.html')
    
    message.setAsRead

    context = {'label':label,'message':message}
    return render(request,'single-message.html',context = context)


@login_required(login_url='login')
def setUnread(request,pk):
    label = "Messages"

    try:
        message = Message.objects.get(id=pk)
    except Message.DoesNotExist:
        return render(request,'notFound.html')

    message.setAsUnread
    messages = Message.objects.all()

    context = {'label':label,'messages':messages}
    return render(request,'messages.html',context = context)


@login_required(login_url='login')
def profile(request):
    label = "Profile"
    user = request.user

    context = {'label':label,'user':user}
    return render(request,'profile.html',context = context)
