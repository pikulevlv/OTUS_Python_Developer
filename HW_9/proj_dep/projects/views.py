from django.shortcuts import render
from .models import Staff, StaffListPosition, Direction, Sertificate
from .models import Project, Stage, Role
# from celery import current_app
from django.views.generic import ListView, DetailView, UpdateView, \
    CreateView, FormView, DeleteView
from .forms import ContactForm, StaffForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        # просто сформулировать условие выдачи прав
        # return self.request.user.email.endswith('@example.com')
        return self.request.user.is_superuser

class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

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


# class StaffCreateView(StaffOnlyMixin, CreateView):
class StaffCreateView(CreateView):
    model = Staff
    template_name = 'projects/edit_create_staff.html'
    success_url = '/'
    # fields = '__all__' # возьмем все поля
    # fields = ('name','card', 'specia', 'age') # перечислим нужные поля
    # исключить ненужные поля можно в формах
    form_class = StaffForm

    def form_valid(self, form):
        user = self.request.user # мы т.к. в форме создания змеи скрывали пользователя
        form.instance.user = user # прописываем его из инстанса формы
        return super().form_valid(form) # сохраняем форму


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'projects/register.html'


# class StaffUpdateView(StaffOnlyMixin, UpdateView):
class StaffUpdateView(UpdateView):
    model = Staff
    template_name = 'projects/edit_create_staff.html'
    success_url = '/'
    # fields = '__all__' # возьмем все поля
    form_class = StaffForm

# class StaffDeleteView(AdminOnlyMixin, DeleteView):
class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'projects/delete_confirm_staff.html'
    success_url = '/'


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

class LoginUserView(LoginView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'projects/login.html'


class LogoutUserView(LogoutView):
    pass
