from django.shortcuts import render
from .models import Student, Cat

def student_list(request):
    # Fetch all students from the database
    students = Student.objects.all()

    # Prepare data for rendering
    student_data = []
    for student in students:
    # Retrieve the cats for the current student and sort them alphabetically
        cats = student.cat_set.all().order_by('name')
        num_cats = cats.count()  # Calculate the number of cats for each student
        student_data.append({'student': student, 'cats': cats, 'num_cats': num_cats})

    # Render the template with the student data
    return render(request, 'students/student_list.html', {'students': student_data})

def about_pets(request):
    # Retrieve all cats from the database (assuming you have a Cat model)
    cats = Cat.objects.all().order_by('name')
    return render(request, 'students/about_pets.html', {'cats': cats})