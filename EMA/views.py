

from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method == 'POST':
        check=request.POST.get('check')
        print(check)
        if check is None :
            isActive = False
        else:
            isActive = True
    date = datetime.datetime.now()
    
    name = "LearnCodeWith Durgesh"
    list_of_programs = [
        'WAP to check even or odd numbers',
        'WAP to check prime number',
        'WAP to print all prime numbers',
        'WAP to print pascals triangles'
    ]
    student = {
        'student_name': 'Rahul',
        'student_college': 'ZYZ',
        'student_city': 'Delhi'
    }
    data={
        'isActive': isActive,
        'name':name,
        'date':date,
        'list_of_programs':list_of_programs,
        'student_data': student
        
    }
    return render(request, 'home.html',data)
def about(request):
    return render(request, 'about.html',{})
def service(request):
    return render(request, 'services.html',{})