from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.decorators import login_required


# Create your views here.
from marker.models import AssessmentSheet, AssessmentSheetForm, LAB_CHOICES

def index(request):

    return render(request, 'marker/index.html', {})

def student(request, lab=0):


    if lab==0:
        as_list = AssessmentSheet.objects.all().order_by('lastname')
        lab = 'All Lab Groups'
    else:
        as_list = AssessmentSheet.objects.filter(lab=int(lab)).order_by('lastname')
        lab = 'Lab Group ' + lab

    for student in as_list:
        mark = tally_mark(student)
        student.mark = mark

    context_dict = {'student_list': as_list, 'lab': lab}

    return render(request, 'marker/students.html', context_dict)

def date(request, year,month):
    return HttpResponse("The year month in the url. " + year + " " + month)

def student_form(request, studentno):

    record = AssessmentSheet.objects.get(studentno=studentno)

    mark = tally_mark(record)

    return render(request, 'marker/completed_assessment_form.html',{'record':record, 'mark': mark})


def tally_mark(record):

    mark = 0.0

    def get_mark(judgement,value):
        mult = {'N':0.0, 'A':0.25, 'C':0.25, 'P':0.5, 'F':1.0}
        mark = mult[judgement] * value
        return mark

    mark += get_mark(record.chapter3,2)
    mark += get_mark(record.chapter4,2)
    mark += get_mark(record.chapter5,2)
    mark += get_mark(record.chapter6,2)
    mark += get_mark(record.chapter7,2)
    mark += get_mark(record.chapter8,3)
    mark += get_mark(record.chapter9,3)
    mark += get_mark(record.chapter10,4)
    mark += get_mark(record.chapter11,5)
    mark += get_mark(record.chapter12,5)
    mark += get_mark(record.chapter13,5)
    mark += get_mark(record.chapter14,5)
    mark += get_mark(record.chapter15,5)
    mark += get_mark(record.chapter16,5)
    mark += get_mark(record.chapter21,5)

    return mark




def enter_sheet(request):

    if request.method == 'POST':
        form = AssessmentSheetForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            mark = tally_mark(record)
            return render(request, 'marker/completed_assessment_form.html',{'record':record, 'mark': mark})
        else:
            print form.errors

    else:
        form = AssessmentSheetForm()

    return render(request, 'marker/assessment_form.html', {'form': form} )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/marker/')
            else:
                return HttpResponse("This account has been disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'marker/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/marker/')