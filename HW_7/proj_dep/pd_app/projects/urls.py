from django.urls import path
from .views import index_view, projects_page_view

app_name = 'projects'

urlpatterns = [
    path('', index_view, name='index'),
    path('projects_page/', projects_page_view, name='projects_page'),
]
