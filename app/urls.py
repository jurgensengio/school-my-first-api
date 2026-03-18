"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import StudentCreateListView, StudentRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentCreateListView.as_view(), name='student-create-list'),
    #se bater na rota students com um get, ele exibe todos os students
    #se bater na rota students com um post, ele cria um aluno
    path('students/<int:pk>', StudentRetrieveUpdateDestroy.as_view(), name='student-detail-view'),
    #se bater na rota students/id com um get, ele exibe o aluno correspondente
    #se bater na rota students/id com um put/patch, ele atualiza o aluno correspondente
    #se bater na rota students/id com um delete, ele deleta o aluno correspondente
]
