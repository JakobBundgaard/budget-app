from django.contrib import admin
from .models import Salary, Budget

class BudgetInline(admin.StackedInline):  # Eller admin.StackedInline for en anden stil
    model = Budget
    extra = 1  # Viser én tom række til at tilføje nye budgetposter direkte

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('gross_income', 'tax_percentage', 'net_income')  # Tilføj vigtige felter
    search_fields = ('gross_income', 'tax_percentage')  # Gør bruttoløn og skat søgbare
    list_filter = ('tax_percentage',) # Gør det muligt at filtrere efter skatteprocent
    ordering = ('-gross_income',)  # Sorterer lønninger i faldende rækkefølge (højeste først)

    # Gruppér felterne i sektioner
    fieldsets = (
        ('Grundlæggende Information', {
            'fields': ('gross_income', 'tax_percentage', 'deductions')
        }),
        ('Beregnet Data', {
            'fields': ('am_contribution', 'taxable_income', 'net_income'),
            'classes': ('collapse',)  # Skjuler sektionen som standard
        }),
    )

    # Gør beregnede felter skrivebeskyttede
    readonly_fields = ('am_contribution', 'taxable_income', 'net_income')

    inlines = [BudgetInline]  # 🔥 Viser alle budgetposter, der hører til denne Salary

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'salary')  # Vis kategori, beløb og tilknyttet løn
    search_fields = ('category',)  # Gør det muligt at søge efter kategori
    list_filter = ('category',) # Gør det muligt at filtrere efter kategori
    ordering = ('-amount',)  # Sorterer budgetposter i faldende rækkefølge (største beløb først)
