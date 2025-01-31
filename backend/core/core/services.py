from decimal import Decimal
from django.db import models
import django.apps  # Lazy import for at undgå cirkulære imports


class SalaryCalculator:
    """ Klasse til at håndtere lønberegninger """
    
    AM_RATE = Decimal("0.08")  # 8% arbejdsmarkedsbidrag

    def __init__(self, gross_income, tax_percentage, deductions=0):
        self.gross_income = Decimal(gross_income)
        self.tax_percentage = Decimal(tax_percentage)
        self.deductions = Decimal(deductions)
    
    def calculate_net_income(self):
        am_contribution = self.gross_income * self.AM_RATE
        taxable_income = self.gross_income - am_contribution - self.deductions
        net_income = taxable_income * (1 - (self.tax_percentage / 100))
        return net_income

    def save_salary(self):
        """ Gem lønnen i databasen """
        Salary = django.apps.apps.get_model('core', 'Salary')  # Lazy import
        net_income = self.calculate_net_income()
        salary = Salary.objects.create(
            gross_income=self.gross_income,
            tax_percentage=self.tax_percentage,
            deductions=self.deductions,
            am_contribution=self.gross_income * self.AM_RATE,
            taxable_income=self.gross_income - self.gross_income * self.AM_RATE - self.deductions,
            net_income=net_income,
        )
        return salary


class BudgetManager:
    """ Klasse til at styre budgettering """

    def __init__(self, salary):
        self.salary = salary  # Salary objekt

    def get_total_budget(self):
        """ Returnerer summen af alle budgetposter tilknyttet en given løn """
        Budget = django.apps.apps.get_model('core', 'Budget')  # Lazy import
        return Budget.objects.filter(salary=self.salary).aggregate(total=models.Sum('amount'))['total'] or Decimal(0)

    def can_add_budget(self, amount):
        """ Tjekker, om det er muligt at tilføje en ny budgetpost uden at overskride nettolønnen """
        total_budget = self.get_total_budget()
        remaining_budget = self.salary.net_income - total_budget
        return amount <= remaining_budget

    def add_budget(self, category, amount):
        """ Tilføjer en ny budgetpost, hvis den ikke overstiger nettolønnen """
        Budget = django.apps.apps.get_model('core', 'Budget')  # Lazy import
        if self.can_add_budget(amount):
            budget = Budget.objects.create(salary=self.salary, category=category, amount=amount)
            return budget
        raise ValueError("Beløbet overstiger din nettoløn!")
