from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializers



class TaskApiView(APIView):
    def get(self, request, detail_id=None):
        if detail_id:
            try:
                task = Task.objects.get(pk=detail_id)
            except Task.DoesNotExist:
                return Response({"Error": 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = TaskSerializers(task)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializers(tasks, many=True)

        return Response({'tasks': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, put_id=None):
        if not put_id:
            return Response({'Error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(pk=put_id)
        except Task.DoesNotExist:
            return Response({'Error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializers(instance=task, data=request.data, partial=True)  # partial=True for partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, put_id=None):
        if not put_id:
            return Response({'Error': 'ID is required for deletion'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.get(pk=put_id)
            task.delete()
            return Response({'Message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({'Error': 'Task not found'}, status=status.HTTP_200_OK)