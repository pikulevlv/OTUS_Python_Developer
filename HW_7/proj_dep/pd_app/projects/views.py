from django.shortcuts import render
from .models import Staff, StaffListPosition, Direction, Sertificate
from .models import Project, Stage, Role

# Create your views here.

def index_view(request):
    staff_units = Staff.objects.all()
    zup_units = Staff.objects.filter(direct__name='ZUP')
    erp_units = Staff.objects.filter(direct__name='ERP')

    exp_units = Staff.objects.filter(salary__gte=155_000)
    context = {
        "staff_units":staff_units,
        "zup_units":zup_units,
        "erp_units":erp_units,
        "exp_units":exp_units,
    }
    return render(request, 'projects/index.html', context)