from django.urls import include, path

from . import views

urlpatterns = [
    path("students/", views.GetStudents.as_view()),
    path("student/<int:pk>/", views.GetStudent.as_view()),
    path("add-student/", views.AddStudent.as_view()),
    path("edit-student/<int:pk>/", views.EditStudent.as_view()),
    path("delete-student/<int:pk>/", views.DeleteStudent.as_view()),
]
