from rest_framework import serializers
from .models import Salary, Budget

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'  # Inkluderer alle felter i JSON-responsen
        extra_kwargs = {
            'tax_percentage': {'required': False},  # 👈 Gør feltet ikke-obligatorisk
            'deductions': {'required': False},
            'am_contribution': {'required': False},
            'taxable_income': {'required': False},
            'net_income': {'required': False},
        }

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'  # Inkluderer alle felter i JSON-responsen
