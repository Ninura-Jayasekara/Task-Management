from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.apiInterface, name="api-dashboard"),
	path('all-tasks/', views.getAllTasks, name="all-tasks"),
	path('search/<str:pk>/', views.getTask, name="search"),
	path('create/', views.addTask, name="create"),

	path('update/<str:pk>/', views.updateTask, name="update"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]