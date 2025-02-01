from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Salary
from .serializers import SalarySerializer

class SalaryListCreateView(APIView):
    def get(self, request):
        salaries = Salary.objects.all()  # Hent alle Salary-objekter
        serializer = SalarySerializer(salaries, many=True)  # Serialisér data
        return Response(serializer.data)  # Returnér som JSON

    def post(self, request):
        serializer = SalarySerializer(data=request.data)  # Modtag data fra brugeren
        if serializer.is_valid():  # Valider data
            serializer.save()  # Gem i databasen
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaryDetailView(APIView):
    def get(self, request, pk):
        salary = get_object_or_404(Salary, pk=pk)
        serializer = SalarySerializer(salary)
        return Response(serializer.data)

    def patch(self, request, pk):
        salary = get_object_or_404(Salary, pk=pk)
        serializer = SalarySerializer(salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        salary = get_object_or_404(Salary, pk=pk)
        salary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)