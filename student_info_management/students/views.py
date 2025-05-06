from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentInfoForm
from .models import StudentInfo
from ml_model.predict import predict_course  # ML function

# Create Student and Update Student
def student_info_view(request, pk=None):
    predicted_course = None  # Default value to pass to the template
    if pk:
        student = get_object_or_404(StudentInfo, pk=pk)
    else:
        student = None

    if request.method == 'POST':
        if student:  # If there's an existing student, populate the form with its data
            form = StudentInfoForm(request.POST, instance=student)
        else:
            form = StudentInfoForm(request.POST)

        selected_course = request.POST.get('course')  # Course selected from dropdown

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            interest = form.cleaned_data['interest']

            # If the user clicked "Suggest Course"
            if 'predict' in request.POST:
                predicted_course = predict_course(age, gender, interest.lower())
                # Render the form again with prediction shown
                return render(request, 'students/student_info_form.html', {
                    'form': form,
                    'predicted_course': predicted_course,
                })

            # Otherwise, treat it as a real submission
            course_to_save = selected_course if selected_course else None

            if student:
                student.name = name
                student.address = address
                student.email = email
                student.gender = gender
                student.age = age
                student.interest = interest
                student.course = course_to_save
                student.save()
            else:
                # Create new student if no student exists
                StudentInfo.objects.create(
                    name=name,
                    address=address,
                    email=email,
                    gender=gender,
                    age=age,
                    interest=interest,
                    course=course_to_save
                )

            return redirect('student_success')

    else:
        if student:  # If there's an existing student, populate the form with its data
            form = StudentInfoForm(instance=student)
        else:
            form = StudentInfoForm()

    return render(request, 'students/student_info_form.html', {
        'form': form,
        'predicted_course': predicted_course,
    })

# Success Page After Creating
def student_success_view(request):
    return render(request, 'students/success.html')


# List Students (Read)
def student_list_view(request):
    students = StudentInfo.objects.all()  # Fetch all students from the database
    return render(request, 'students/student_list.html', {'students': students})

def student_view(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)  # Get the student by primary key
    return render(request, 'students/student_view.html', {'student': student})



# Delete Student (Delete)
def student_delete_view(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)

    if request.method == 'POST':
        student.delete()  # Delete the student record
        return redirect('student_list')  # Redirect to student list page

    return render(request, 'students/student_confirm_delete.html', {'student': student})
