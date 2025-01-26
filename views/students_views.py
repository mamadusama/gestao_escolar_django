from django.http import HttpResponse
from django.shortcuts import redirect, render

from entities import  students, usuario
from forms.students_form import StudentForm
from services import student_service


def create_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():

            # Dados do Estudante
            first_name = student_form.cleaned_data["first_name"]
            last_name = student_form.cleaned_data["last_name"]
            date_of_birth = student_form.cleaned_data["date_of_birth"]
            gender = student_form.cleaned_data["gender"]
            nationality = student_form.cleaned_data["nationality"]
            phone_number = student_form.cleaned_data["phone_number"]
            email = student_form.cleaned_data["email"]
            address = student_form.cleaned_data["address"]
            city = student_form.cleaned_data["city"]
            neighborhood = student_form.cleaned_data["neighborhood"]
            postal_code = student_form.cleaned_data["postal_code"]
            profile_img = student_form.cleaned_data["profile_img"]
            usuario= student_form.cleaned_data["usuario"]
            parent= student_form.cleaned_data["parent"]


            new_student = students.StudentEntity(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                nationality=nationality,
                phone_number=phone_number,
                email=email,
                address=address,
                city=city,
                neighborhood=neighborhood,
                postal_code=postal_code,
                profile_img=profile_img,
                usuario = usuario,
                parent=parent
            )

            student_service.register_student(new_student)

            return redirect("students_list")
    else:
        student_form = StudentForm()

    return render(request,"students/create_student.html",{"student_form": student_form,
          
        },
    )

# ----- cruds adicionais -------

def list_students(request):
    students = student_service.get_all_students()
    return render(request, "students/list_students.html", {"students": students})



def student_list_by_id(request, id):
    """
    Exibe detalhes de um estudante específico. no perfil
    """
    student = student_service.get_student_by_id(id)

    if not student:
        return render(request, "student/page_not_found.html")
    return render(request, "students/student_page_profile.html", {"student": student})




def update_student(request, student_id):
    """
    Atualiza os dados de um estudante específico.
    """
    student = student_service.get_student_by_id(student_id)
    if not student:
        return HttpResponse("Estudante não encontrado", status=404)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/update_student.html", {"form": form, "student": student})


def delete_student(request, student_id):
    """
    Exclui um estudante específico.
    """
    student = student_service.get_student_by_id(student_id)
    if not student:
        return HttpResponse("Estudante não encontrado", status=404)

    if request.method == "POST":
        student_service.delete_student(student_id)
        return redirect("students_list")

    return render(request, "students/delete_student.html", {"student": student})