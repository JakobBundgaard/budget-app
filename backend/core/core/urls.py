
from django.contrib import admin
from django.urls import path
from .views import SalaryListCreateView, SalaryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/salaries/', SalaryListCreateView.as_view(), name='salary-list-create'),
    path('api/salaries/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
]
