from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class StudentView(APIView):

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            student = Student.objects.get(id=kwargs['pk'])
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        elif 'date_joined' in kwargs:
            students = Student.objects.filter(date_joined=kwargs['date_joined'])
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        else:
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many = True)
            return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    
    #delete
    def delete(self, request, pk, *args, **kwargs):
        post = Student.objects.get(id=pk)
        post.delete()
        return Response()

    #update / put
    def put(self, request, pk, *args, **kwargs):
        post = Student.objects.get(id=pk)
        serializer = StudentSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)







