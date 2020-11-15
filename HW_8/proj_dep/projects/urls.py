from django.urls import path
from .views import projects_page_view, roles_page_view
from .views import StaffListView, ContactFormView, StaffDetailView

app_name = 'projects'

urlpatterns = [
    path('', StaffListView.as_view(), name='index'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('projects_page/', projects_page_view, name='projects_page'),
    path('roles_page/', roles_page_view, name='roles_page'),
    path('contact_page/', ContactFormView.as_view(), name='contact_page'),
]
