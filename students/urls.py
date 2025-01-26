from django.urls import path

from views import students_views  # Import das views centralizadas

urlpatterns = [
    path("create_student/", students_views.create_student , name="create_student"),
    path("students_list/", students_views.list_students, name="students_list"),
    path("student_list_by_id/<int:id>", students_views.student_list_by_id, name="student_list_by_id"), 
    
  
]
"""   path("student_list_by_id/<int:id>", students_views.student_list_by_id, name="student_list_by_id"), """