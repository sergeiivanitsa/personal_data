from tabnanny import verbose
from django.db import models
import personal_data.settings as settings

class Statement(models.Model):
    '''Модель для создания записи в БД с персональными занными заявителя и 
    данными банковского договора'''

    # время добавления записи
    pub_date = models.DateTimeField(auto_now_add=True)
    # имя
    firstname = models.CharField(max_length=20, verbose_name = "")
    # фамилия
    lastname = models.CharField(max_length=20, verbose_name = "")
    # отчество
    middlename = models.CharField(max_length=20, verbose_name = "")
    # дата рождения
    birth_date = models.DateField(auto_now_add=False, default="01.01.1990", verbose_name = "")
    # место рождения
    birth_place = models.CharField(max_length=200, verbose_name = "")
    # серия паспорта
    pass_serie = models.CharField(max_length=4, verbose_name = "")
    # номер паспорта
    pass_number = models.CharField(max_length=6, verbose_name = "")
    # код подразделения
    division_code = models.CharField(max_length=12, verbose_name = "")
    # дата выдачи паспорта
    issue_date = models.DateField(auto_now_add=False, default="01.01.2010", verbose_name = "")
    # кем выдан паспорт
    whom_issued = models.CharField(max_length=500, verbose_name = "")
    # адрес места регистрации
    address = models.CharField(max_length=500, verbose_name = "")

    # банковские данные
    # название банка
    bank_name = models.CharField(max_length=500, verbose_name = "")
    # данные банка
    bank_data = models.CharField(max_length=500, verbose_name = "")
    # дата заключения договора
    contract_date = models.DateField(auto_now_add=False, default="01.01.2022", verbose_name = "")
    # номер договора
    contract_number = models.CharField(max_length=50, verbose_name = "")