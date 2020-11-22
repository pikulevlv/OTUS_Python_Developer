from django.urls import path
from .views import projects_page_view, roles_page_view
from .views import StaffListView, ContactFormView, StaffDetailView, StaffCreateView,\
    StaffUpdateView, StaffDeleteView, UserCreateView, LoginUserView, LogoutUserView

app_name = 'projects'

urlpatterns = [
    path('', StaffListView.as_view(), name='index'),

    path('registry/', UserCreateView.as_view(), name='registry'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('create/', StaffCreateView.as_view(), name='create'),
    path('staff/<int:pk>/update/', StaffUpdateView.as_view(), name='update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='delete'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),

    path('projects_page/', projects_page_view, name='projects_page'),
    path('roles_page/', roles_page_view, name='roles_page'),
    path('contact_page/', ContactFormView.as_view(), name='contact_page'),
]
