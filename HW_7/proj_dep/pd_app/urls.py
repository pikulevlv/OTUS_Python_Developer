from django.contrib import admin
from django.urls import path, include

import debug_toolbar
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls', namespace='projects')),
    path('__debug__/', include(debug_toolbar.urls)),

]
