from django.urls import path

from .api import EmpRoutineAPI

urlpatterns = [
    path('employee-routine', EmpRoutineAPI.as_view(), name='article_list'),
    ]
