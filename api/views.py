from core.models import Students
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view as api
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from employees.models import Employees
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework import generics

# Create your views here.


# FUNCTION BASED VIEWS

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
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
# FUNCTION BASED VIEWS

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
    
    
    
# CLASS BASED VIEWS

# class Employee(APIView):
#     def get(self, request):
#         employee = Employees.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# CLASS BASED VIEWS

# class EmployeeViewDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employees.objects.get(pk=pk)
#         except Employees.DoesNotExist:
#             return Http404
        
#     def get (self, request, pk):
#         employee = Employees.objects.get(pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put (self, request, pk):
#         employee = Employees.objects.get(pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete (self, request, pk):
#         employee = Employees.objects.get(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
# MIXINS VIEWS
# class Employee(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# MIXINS VIEWS
# class EmployeeViewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employees.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)
    
    
    
# GENERIC VIEWS
class Employee(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


# GENERIC VIEWS
class EmployeeViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer