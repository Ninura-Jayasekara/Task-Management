from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Task
from .serializers import TaskSerializer

#dashboard

@api_view(['GET'])
def apiInterface(request):
	api_urls = {
		'All Tasks':'/all-tasks/',
		'Search':'/search/<str:pk>/',
		'Create':'/create/',
		'Update':'/update/<str:pk>/',
		'Delete':'/delete/<str:pk>/',
		}

	return Response(api_urls)

#get method for fetching all data

@api_view(['GET'])
def getAllTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer (tasks, many ='True')
    return Response(serializer.data)

#get method for search by id

@api_view(['GET'])
def getTask(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

#post method to add a new task

@api_view(['POST'])
def addTask(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#method to update task

@api_view(['POST'])
def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#method to delete a task

@api_view(['DELETE'])
def deleteTask(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Task Deleted succsesfully !')


