from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('departments', views.departments, name='departments'),
    path('create_department', views.create_department, name='create_department'),
    path('department/<int:pk>', views.departmentDetailView.as_view(), name='department_detail'),
    path('department/<int:pk>/update', views.departmentUpdateView.as_view(), name='department_update'),
    path('department/<int:pk>/delete', views.departmentDeleteView.as_view(), name='department_delete'),
    path('staff', views.staff, name='staff'),
    path('create_employee', views.create_employee, name='create_employee'),
    path('employee/<int:pk>', views.employeeDetailView.as_view(), name='employee_detail'),
    path('employee/<int:pk>/update', views.employeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete', views.employeeDeleteView.as_view(), name='employee_delete'),
    path('this_department/<int:department_id>/', views.show_department, name='this_department'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('Register', views.Register.as_view(), name="Register"),
    path('LogoutView', views.LogoutView.as_view(), name="logout"),
    path('LoginFormView', views.LoginFormView.as_view(), name="login"),
]