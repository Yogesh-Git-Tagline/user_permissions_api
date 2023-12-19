from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import *
from rest_framework.permissions import (AllowAny, DjangoModelPermissions,
                                        IsAdminUser, IsAuthenticated)

from .models import Student
from .serializer import StudentSerializer


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
