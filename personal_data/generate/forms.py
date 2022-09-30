from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm

from .models import Statement  # Импортируем модель, чтобы связать с ней форму

class GenerateForm(forms.ModelForm):
    class Meta:
        # Эта форма будет работать с моделью
        model = Statement
        # Здесь перечислим поля модели, которые должны отображаться в веб-форме;
        # при необходимости можно вывести в веб-форму только часть полей из модели.
        fields = ('firstname', 'lastname', 'middlename',
                  'birth_date', 'birth_place', 'pass_serie', 'pass_number',
                  'division_code', 'issue_date', 'whom_issued', 'address',
                  'bank_name', 'bank_data', 'contract_date', 'contract_number'
                  )
