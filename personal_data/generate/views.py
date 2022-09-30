from django.views.generic.edit import CreateView
from .forms import GenerateForm
from django.shortcuts import redirect, render
from pathlib import Path

from .makestatement import makestatement, fakestatement
from .models import Statement

from django.http import FileResponse


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

           # return FileResponse(open('output.pdf', 'rb'), as_attachment=True)
            return render(request, 'generate/thankyou.html')
        return render(request, 'generate/generate.html', {'form': form})
    return render(request, 'generate/generate.html', {'form': form})


def success(request):
    template = 'generate/thankyou.html'
    return render(request, template)
