from rest_framework import generics
from teachers.models import Teacher
from teachers.serializers import TeacherSerializers

class TeacherCreateListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all() #pega todos os Teachers da tabela = select * from Teachers
    serializer_class = TeacherSerializers #transforma o objeto em JSON ou JSON em objeto


class TeacherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers