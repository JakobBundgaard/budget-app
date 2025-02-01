from rest_framework import serializers
from .models import Salary, Budget

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'  # Inkluderer alle felter i JSON-responsen

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'  # Inkluderer alle felter i JSON-responsen
