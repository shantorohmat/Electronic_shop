from typing import ValuesView
from django.urls import path
from django.urls import path
from .import views 

urlpatterns = [
    path('projects/',views.projects,name="projects"),
    path('projects/create-project/',
        views.create_project,name="create_project"),
    path('projects/<str:project_id>/',
        views.project_detail, name="project_detail"), 
    path('projects/update-project/<str:project_id>/',
        views.edit_project, name="edit_project"),  
     path('projects/delete-project/<str:project_id>/', views.delete_project,name="delete_project" ),
]
