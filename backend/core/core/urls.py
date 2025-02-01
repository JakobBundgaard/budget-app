
from django.contrib import admin
from django.urls import path
from .views import SalaryListCreateView, SalaryDetailView, BudgetListCreateView, BudgetDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/salaries/', SalaryListCreateView.as_view(), name='salary-list-create'),
    path('api/salaries/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
    path('api/budgets/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('api/budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
]
