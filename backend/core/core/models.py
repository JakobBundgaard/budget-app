from django.db import models

class Salary(models.Model):
    """Model til at gemme information om løn før og efter skat"""
    gross_income = models.DecimalField(max_digits=10, decimal_places=2)  # Bruttoløn
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Skatteprocent
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Fradrag
    am_contribution = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # AM-bidrag (8%)
    taxable_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Skattepligtig indkomst
    net_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Nettoløn

    def save(self, *args, **kwargs):
        """Automatisk beregn AM-bidrag, skattepligtig indkomst og nettoløn før gemning"""
        self.am_contribution = self.gross_income * 0.08  # 8% arbejdsmarkedsbidrag
        self.taxable_income = self.gross_income - self.am_contribution - self.deductions  # Skattepligtig indkomst
        self.net_income = self.taxable_income * (1 - (self.tax_percentage / 100))  # Nettoløn
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Løn: {self.gross_income} DKK (Netto: {self.net_income} DKK)"

class Budget(models.Model):
    """Model til at gemme brugerens budgetplan"""
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)  # Tilknyt en løn
    category = models.CharField(max_length=255)  # F.eks. 'Bolig', 'Mad', 'Transport'
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Budgeteret beløb

    def __str__(self):
        return f"{self.category}: {self.amount} DKK"
