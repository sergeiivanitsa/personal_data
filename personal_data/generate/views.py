from django.views.generic.edit import CreateView
from .forms import GenerateForm
from django.shortcuts import redirect, render
from pathlib import Path
import time
from django.template.response import TemplateResponse

from .makestatement import makestatement, fakestatement
from .pdftojpg import makejpg
from .models import Statement

from django.http import FileResponse

from .payment import paylink


def statement_generate(request):
    form = GenerateForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.save()
            set = Statement.objects.latest('pub_date')

            # банковские данные
            bank_name = set.bank_name
            bank_data = set.bank_data
            contract_date = set.contract_date
            contract_number = set.contract_number

            # персональные данные
            firstname = set.firstname
            lastname = set.lastname
            middlename = set.middlename
            birth_date = set.birth_date
            birth_place = set.birth_place
            pass_serie = set.pass_serie
            pass_number = set.pass_number
            division_code = set.division_code
            issue_date = set.issue_date
            whom_issued = set.whom_issued
            address = set.address
            id = set.id
            
            makestatement(firstname, lastname, middlename, birth_date, birth_place, pass_serie, 
                          pass_number, division_code, issue_date, whom_issued, address, bank_name, 
                          bank_data, contract_date, contract_number, id)
            
            fakestatement(firstname, lastname, middlename, birth_date, birth_place, pass_serie, 
                          pass_number, division_code, issue_date, whom_issued, address, bank_name, 
                          bank_data, contract_date, contract_number, id)

            makejpg(id)

            #paymentlink = paylink(id) http://localhost:8000/

            paymentlink = 'https://ya.ru/'



            print(paymentlink)

            data = {"url" : f'/media/images/{id}.jpg', 
                    "paymentlink" : f'{paymentlink}'}

            return TemplateResponse(request, 'generate/success.html', context=data)
        return render(request, 'generate/generate.html', {'form': form})
    return render(request, 'generate/generate.html', {'form': form})


def success(request):
    template = 'generate/success.html'
    return render(request, template)
