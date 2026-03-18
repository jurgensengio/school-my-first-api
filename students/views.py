from rest_framework import generics
from students.models import Student
from students.serializers import StudentSerializers

class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all() #pega todos os students da tabela = select * from students
    serializer_class = StudentSerializers #transforma o objeto em JSON ou JSON em objeto


class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers