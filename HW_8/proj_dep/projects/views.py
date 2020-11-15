from django.shortcuts import render
from .models import Staff, StaffListPosition, Direction, Sertificate
from .models import Project, Stage, Role
# from celery import current_app
from django.views.generic import ListView, DetailView, UpdateView, CreateView, FormView
from .forms import ContactForm

# Create your views here.

class StaffListView(ListView):
    model = Staff # Модель, которую нужно вывести в список
    template_name = 'projects/index.html' # в какой шаблон выведем данные

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = '1'
        return context


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'projects/staff_detail.html'


def projects_page_view(request):
    project_units = Project.objects.all()
    context = {"project_units": project_units}
    context['active_page'] = '1'
    return render(request, 'projects/projects_page.html', context)

def roles_page_view(request):
    role_units = Role.objects.all()
    context = {"role_units": role_units}
    context['active_page'] = '1'
    return render(request, 'projects/roles_page.html', context)

class ContactFormView(FormView):
    template_name = "projects/contact_page.html"
    form_class = ContactForm
    success_url = '/'