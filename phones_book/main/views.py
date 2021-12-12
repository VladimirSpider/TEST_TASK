from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Department, Staff
from .forms import DepartmentForm, StaffForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.views.generic.base import View

# Create your views here.


def index(request):
    # return HttpResponse("<h1>Главная страница!<h1>")
    #staff = Staff.objects.all()
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
    staff = ''
    if search == '':
        staff = Staff.objects.all()
    else:
        staff = Staff.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
    department = Department.objects.all()
    context = {
        'staff': staff,
        'departments': department,
        'title': 'Главная страница',
        'dep_selected': 0,
    }
    return render(request, "main/index.html", context)


def show_department(request, department_id):
    #return HttpResponse(f"Отображение отдела с id = {department_id}")
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
    staff = ''
    if search == '':
        staff = Staff.objects.filter(department_id=department_id)
    else:
        staff = Staff.objects.filter((Q(first_name__icontains=search) | Q(last_name__icontains=search)) & Q(department_id=department_id))

    department = Department.objects.all()

    #if len(staff) == 0:
    #    raise Http404()

    context = {
        'staff': staff,
        'departments': department,
        'title': 'Отображение по отделам',
        'dep_selected': department_id,
    }
    return render(request, 'main/index.html', context=context)
#-------------------------------------------------------
def departments(request):
    #return HttpResponse("<h1>Наши отделы!<h1>")
    departments = Department.objects.all()
    return render(request, "main/departments.html", {'title' : 'Отделы',
                                                     'departments': departments,
                                                     'dep_selected': 'departments',})

class departmentDetailView(DetailView):
    model = Department
    template_name = 'main/detail_department.html'
    context_object_name = 'department'

class departmentUpdateView(UpdateView):
    model = Department
    template_name = 'main/update_department.html'
    form_class = DepartmentForm
    context_object_name = 'department'

class departmentDeleteView(DeleteView):
    model = Department
    success_url = '/departments'
    template_name = 'main/delete_department.html'
    context_object_name = 'department'

def create_department(request):
    error = ''
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
        else:
            error = 'Форма была не верной!'
    form = DepartmentForm()
    data = {'title': 'Создание отдела',
            'form': form,
            'error': error,
    }
    return render(request, "main/create_department.html", data)
#-------------------------------------------------------
def staff(request):
    departments = Department.objects.all()
    staff = Staff.objects.all().order_by('department')
    return render(request, "main/staff.html", {'title' : 'Сотрудники',
                                               'departments': departments,
                                               'staff': staff,
                                               'dep_selected': 'staff'})

class employeeDetailView(DetailView):
    model = Staff
    template_name = 'main/detail_employee.html'
    context_object_name = 'employee'

class employeeUpdateView(UpdateView):
    model = Staff
    template_name = 'main/update_employee.html'
    form_class = StaffForm
    context_object_name = 'employee'

class employeeDeleteView(DeleteView):
    model = Staff
    success_url = '/staff'
    template_name = 'main/delete_employee.html'
    context_object_name = 'employee'
def create_employee(request):
    error = ''
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('staff')
        else:
            error = 'Форма была не верной!'
    form = StaffForm()
    data = {'title': 'Добавление сотрудника',
            'form': form,
            'error': error,
    }
    return render(request, "main/create_employee.html", data)



def registration_page(request):
    return render(request, 'main/registration_page.html', {'dep_selected': 'registration'})

class Register(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "main/register.html"

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/registration_page")

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "main/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)