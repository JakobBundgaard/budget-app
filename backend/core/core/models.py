from django.db import models
import django.apps  # Lazy import for at undgå cirkulære imports


class Salary(models.Model):
    gross_income = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    am_contribution = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    taxable_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        """ Brug SalaryCalculator fra services.py via lazy import """
        SalaryCalculator = django.apps.apps.get_model('core', 'SalaryCalculator')  # Lazy import
        calculator = SalaryCalculator(self.gross_income, self.tax_percentage, self.deductions)

        self.am_contribution = calculator.gross_income * SalaryCalculator.AM_RATE
        self.taxable_income = calculator.gross_income - self.am_contribution - self.deductions
        self.net_income = calculator.calculate_net_income()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Løn: {self.gross_income} DKK (Netto: {self.net_income} DKK)"


class Budget(models.Model):
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category}: {self.amount} DKK"

    @staticmethod
    def create_budget(salary, category, amount):
        """ Brug BudgetManager fra services.py via lazy import """
        BudgetManager = django.apps.apps.get_model('core', 'BudgetManager')  # Lazy import
        manager = BudgetManager(salary)
        return manager.add_budget(category, amount)
