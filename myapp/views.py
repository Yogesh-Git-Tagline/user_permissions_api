from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import *
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions, IsAdminUser
from rest_framework.authentication import SessionAuthentication


class GetStudents(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]


class GetStudent(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]


class AddStudent(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


class EditStudent(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]


class DeleteStudent(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
