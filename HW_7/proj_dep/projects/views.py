from django.shortcuts import render
from .models import Staff, StaffListPosition, Direction, Sertificate
from .models import Project, Stage, Role

# Create your views here.

def index_view(request):
    staff_units = Staff.objects.all()
    project_units = Project.objects.all()
    context = {
        "staff_units": staff_units,
        "project_units": project_units,
    }
    return render(request, 'projects/index.html', context)

def projects_page_view(request):
    project_units = Project.objects.all()
    context = {
        "project_units": project_units,
    }
    return render(request, 'projects/projects_page.html', context)