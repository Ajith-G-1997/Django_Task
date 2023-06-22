from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy


def HomeView(request):
    return render(request, 'student/base.html')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_login.html'
    success_url = reverse_lazy('success')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_view')
    else:
        form = StudentForm()
    
    return render(request, 'student/student_login.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/students_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student/student_details.html', {'student': student})

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('update_view')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student/update.html', {'form': form})



def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)  # Retrieve the student or return 404 if not found

    if request.method == 'POST':
        student.delete()
        return redirect('delete_view')

    return render(request, 'student/delete.html', {'student': student})



def success_view(request):
    return render(request, 'student/success.html')


def update_view(request):
    return render(request, 'student/update_view.html')


def delete_view(request):
    return render(request, 'student/delete_view.html')

def TotalStudents(request):
    students = Student.objects.all()
    return render(request, 'student/total_students.html', {'students': students})