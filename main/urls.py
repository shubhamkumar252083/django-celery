
from django.contrib import admin
from django.urls import path
from check.views import list_view,add_view,task_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/', list_view, name='list_view'),
    path('add/', add_view, name='add_view'),
    path('status/<str:task_id>/', task_status, name='task_status'),
]

