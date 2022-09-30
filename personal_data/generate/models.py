from django.db import models
import personal_data.settings as settings

class Statement(models.Model):
    '''Модель для создания записи в БД с персональными занными заявителя и 
    данными банковского договора'''

    # время добавления записи
    pub_date = models.DateTimeField(auto_now_add=True)
    # имя
    firstname = models.CharField(max_length=20)
    # фамилия
    lastname = models.CharField(max_length=20)
    # отчество
    middlename = models.CharField(max_length=20)
    # дата рождения
    birth_date = models.DateField(auto_now_add=False, default="01.01.1990")
    # место рождения
    birth_place = models.CharField(max_length=200)
    # серия паспорта
    pass_serie = models.CharField(max_length=4)
    # номер паспорта
    pass_number = models.CharField(max_length=6)
    # код подразделения
    division_code = models.CharField(max_length=12)
    # дата выдачи паспорта
    issue_date = models.DateField(auto_now_add=False, default="01.01.2010")
    # кем выдан паспорт
    whom_issued = models.CharField(max_length=500)
    # адрес места регистрации
    address = models.CharField(max_length=500)

    # банковские данные
    # название банка
    bank_name = models.CharField(max_length=500)
    # данные банка
    bank_data = models.CharField(max_length=500)
    # дата заключения договора
    contract_date = models.DateField(auto_now_add=False, default="01.01.2022")
    # номер договора
    contract_number = models.CharField(max_length=50)