from django.db import models
from django.urls import reverse

# Create your models here.

class Department(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')
    staff_count = models.IntegerField('Количество сотрудников')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  f'/department/{self.id}'

    def get_url(self):
        return reverse('this_department', kwargs={'department_id': self.pk})

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Staff(models.Model):
    first_name = models.CharField('Имя', max_length=50, null=True)
    last_name = models.CharField('Фамилия', max_length=50, null=True)
    phone = models.IntegerField('Телефон', null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    post = models.CharField('Должность', max_length=50, null=True)
    experience = models.IntegerField('Стаж', null=True)
    date = models.DateField('Дата приема на работу', null=True)



    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return  f'/employee/{self.id}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'