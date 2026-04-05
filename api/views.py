from core.models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view as api
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from employees.models import Employees

# Create your views here.

@api(['GET', 'POST'])
def students_view(request):
    # student_data = {
    #     'id': 1, 
    #     'name': 'Sameer', 
    #     'height': '182.7cm'
    # }
    # manual way of serializing data
    # student_data = Students.objects.all()
    # print(student_data)
    # students_list = list(student_data.values())
    # return JsonResponse(students_list, safe=False)
    
    # using serializer
    if request.method == 'GET':
        student_data = Students.objects.all()
        serializer = StudentSerializer(student_data, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class Employee(APIView):
    pass

class EmployeeViewDetail(APIView):
    pass