
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Student
from .forms import StudentForm


# Display and search students
def student_list(request):
    query = request.GET.get('q', '').strip()

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(course__icontains=query)
        )

    return render(
        request,
        'students/student_list.html',
        {
            'students': students,
            'query': query
        }
    )


# Add a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )


# Edit student details
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/edit_student.html',
        {
            'form': form,
            'student': student
        }
    )


# Delete student with confirmation
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'students/delete_student.html',
        {'student': student}
    )
