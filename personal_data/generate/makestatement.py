# from borb.pdf.canvas.layout.list.unordered_list import UnorderedList
from atexit import register
from pytrovich.enums import NamePart, Gender, Case
from pytrovich.maker import PetrovichDeclinationMaker

from pathlib import Path
from tkinter.font import Font

from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF

from borb.pdf.canvas.layout.layout_element import Alignment

from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont

# банковские данные
# bank_name = "Публичное акционерное общество «Восточный Экспресс Банк» "
# bank_data = "(Генеральная лицензия Банка России № 1460 от 24.10.2014 г.), 675000, Амурская обл., г. Благовещенск, пер. Святителя Иннокентия, 1"
# contract_date = "28.05.2020"
# contract_number = "20/0201/00000/100709"

# персональные данные
# firstname = "Сергей"
# lastname = "Иваница"
# middlename = "Александрович"
# birth_date = "13.06.1993"
# birth_place = "СЕЛО БАШМАК ЛЕНИНСКОГО Р-НА ЕВРЕЙСКОЙ АВТОНОМНОЙ ОБЛАСТИ"
# pass_serie = "0813"
# pass_number = "179399"
# division_code = "270-026"
# issue_date = "28.08.2013"
# whom_issued = "ОУФМС РОССИИ ПО ХАБАРОВСКОМУ КРАЮ В СЕВЕРНОМ ОКРУГЕ Г. ХАБАРОВСКА"
# address = "Россия, Хабаровский край, г. Хабаровск, переулок Донской 3, кв. 71"

def makestatement(firstname, lastname, middlename, birth_date, birth_place, 
                  pass_serie, pass_number, division_code, issue_date, whom_issued, 
                  address, bank_name, bank_data, contract_date, contract_number, id):

    # create an empty Document
    pdf = Document()

    # add an empty Page
    page = Page()
    pdf.add_page(page)

    # use a PageLayout (SingleColumnLayout in this case)
    layout = SingleColumnLayout(page)

    # construct the Font object
    font_path: Path = Path(__file__).parent / "Vollkorn-Regular.ttf"
    custom_font: Font = TrueTypeFont.true_type_font_from_file(font_path)

    # запускаем петровича
    maker = PetrovichDeclinationMaker()

    # add a Paragraph object
    layout.add(Paragraph("Оператору персональных данных", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    layout.add(Paragraph(f'В {bank_name}', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    layout.add(Paragraph(f'От {maker.make(NamePart.LASTNAME, Gender.MALE, Case.GENITIVE, lastname)} '
                     f'{maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.GENITIVE, firstname)} '
                     f'{maker.make(NamePart.MIDDLENAME, Gender.MALE, Case.GENITIVE, middlename)} '
                     f'(паспорт {pass_serie} {pass_number})', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    layout.add(Paragraph(f"Адрес: {address}", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # технический отступ
    layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # шрифт BOLD
    font_path_bold: Path = Path(__file__).parent / "Vollkorn-Bold.ttf"
    custom_font_bold: Font = TrueTypeFont.true_type_font_from_file(font_path_bold)

    # заголовок
    layout.add(Paragraph("ЗАЯВЛЕНИЕ ОБ ОТЗЫВЕ СОГЛАСИЯ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ", horizontal_alignment=Alignment.CENTERED, font=custom_font_bold, font_size=9))

    # технический отступ
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # первый абзац
    layout.add(Paragraph(f'Между мной, '
                     f'{maker.make(NamePart.LASTNAME, Gender.MALE, Case.INSTRUMENTAL, lastname)} '
                     f'{maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.INSTRUMENTAL, firstname)} '
                     f'{maker.make(NamePart.MIDDLENAME, Gender.MALE, Case.INSTRUMENTAL, middlename)} '
                     f'({birth_date} года рождения, место рождения: {birth_place}, '
                     f'паспорт РФ: {pass_serie} №{pass_number}, код подразделения: {division_code}, выдан: {issue_date} г. ' 
                     f'{whom_issued}, '
                     f'зарегистрирован по адресу: {address}), '
                     f'и Вами, {bank_name}{bank_data} '
                     f'{contract_date} года заключен кредитный договор № {contract_number}. '
                     f'При заключении кредитного договора мною как субъектом '
                     f'персональных данных Вам как Оператору персональных '
                     f'данных было дано согласие на обработку моих '
                     f'персональных данных."', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    #   второй абзац
    layout.add(Paragraph(f'Согласно Федерального Закона РФ N 152-ФЗ "О '
                     f'персональных данных", под обработкой Оператором '
                     f'персональных данных понимается, в том числе, '
                     f'использование и уточнение данных. Статьей 9 пунктом 2 '
                     f'указанного Федерального Закона мне дано право отозвать '
                     f'у Вас и связанных с Вами организаций ранее '
                     f'предоставленное мною право на обработку '
                     f'персональных данных.', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # третий абзац
    layout.add(Paragraph(f'Настоящий отзыв права на использование персональных данных касается: '
                     f'всех контактных телефонов и данных третьих лиц указанных, мною в кредитной документации; '
                     f'адреса проживания моих родственников; '
                     f'адреса и наименования моего работодателя.', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # четвертый абзац
    layout.add(Paragraph(f'Обращаю внимание, что отзыв права на использование моих '
                     f'персональных данных в отдельной части не нарушает Ваши '
                     f'права или права третьих лиц, поскольку контакты Вы со '
                     f'мною может осуществлять через почтовую связь и '
                     f'электронную почту. Кроме того, Вы и Ваши представители '
                     f'не уполномочены законодательством России осуществлять '
                     f'какие-либо розыскные мероприятия, для чего требовались '
                     f'бы отзываемые данные. Вопросы досудебного урегулирования '
                     f'просроченной задолженности предлагаю осуществлять '
                     f'почтовой связью. Если у Вас имеются ко мне претензии, '
                     f'то Вы их можете разрешить в судебном порядке. Таким '
                     f'образом, необходимость использования Вами указанных '
                     f'персональных данных в настоящий момент отпала. Обращаю '
                     f'внимание, что при заключении кредитного договора мною '
                     f'не давалось разрешение на передачу моих персональных '
                     f'данных и их использование третьими лицами '
                     f'(коллекторами). Отмечаю, что при заключении договора '
                     f'мои родственники и прочие контактные лица не давали '
                     f'вам права на использование их персональных данных. В '
                     f'связи с чем, любые звонки и обращения к этим лицам – '
                     f'неправомерны и повлекут их самостоятельное обращение '
                     f'в Роскомнадзор РФ.', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # пятый абзац
    layout.add(Paragraph(f'Одновременно напоминаю и заявляю Вам и связанным с Вами '
                     f'организациям, что я не давал права Вашим представителям '
                     f'посещать меня дома, посещать моих родственников или '
                     f'посещать моего работодателя, так же как не давал права '
                     f'распространять информацию, содержащую банковскую тайну '
                     f'и персональные данные третьим лицам.Запрещаю Вам и '
                     f'связанным с Вами организациям любым образом '
                     f'распространять и публиковать информацию о моей '
                     f'задолженности, не считая предоставления сведений в БКИ.', 
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # шестой абзац
    layout.add(Paragraph(f'Руководствуясь нормами ФЗ РФ № 152-ФЗ «О персональных данных» прошу: '
                     f'c момента получения данного Заявления прошу прекратить '
                     f'обработку моих персональных данных в указанной части; '
                     f'уведомить меня о результатах рассмотрения данного '
                     f'заявления письменно в течение 10 дней с момента его '
                     f'получения. Ответ на заявление прошу направить по '
                     f'почте по адресу указанному выше.',
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # седьмой абзац
    layout.add(Paragraph(f'Уведомляю, что в случае поступления мне или моим '
                     f'контактным лицам телефонных звонков, смс сообщений'
                     f'– буду расценивать данные действия как самоуправство '
                     f'и нарушение неприкосновенности моей частной жизни.В '
                     f'случае, если Вы неправомерно передали мои персональные '
                     f'данные третьему лицу, требую самостоятельного уведомления '
                     f'Вами этой организации об отзыве персональных данных и '
                     f'возможных юридических последствиях, связанных с '
                     f'нарушением Федерального законодательства РФ «О персональных '
                     f'данных». В неполучения ответа на данное обращение, мною будут '
                     f'поданы жалобы: в Прокуратуру РФ, в Роскомнадзор РФ, в Суд, в '
                     f'Центральный Банк РФ.',
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))               

    # технические отступы
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    #  подпись
    layout.add(Paragraph(f'{lastname} {firstname} {middlename}',
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))             

    # store the PDF
    with open(Path(f"outputs/statements/{id}.pdf"), "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)


def fakestatement(firstname, lastname, middlename, birth_date, birth_place, 
                  pass_serie, pass_number, division_code, issue_date, whom_issued, 
                  address, bank_name, bank_data, contract_date, contract_number, id):

    # create an empty Document
    pdf = Document()

    # add an empty Page
    page = Page()
    pdf.add_page(page)

    # use a PageLayout (SingleColumnLayout in this case)
    layout = SingleColumnLayout(page)

    # construct the Font object
    font_path: Path = Path(__file__).parent / "Vollkorn-Regular.ttf"
    custom_font: Font = TrueTypeFont.true_type_font_from_file(font_path)

    # запускаем петровича
    maker = PetrovichDeclinationMaker()

    # add a Paragraph object
    layout.add(Paragraph("********* ************ ****", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    layout.add(Paragraph(f'В {bank_name}', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    layout.add(Paragraph(f'От {maker.make(NamePart.LASTNAME, Gender.MALE, Case.GENITIVE, lastname)} '
                     f'{maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.GENITIVE, firstname)} '
                     f'{maker.make(NamePart.MIDDLENAME, Gender.MALE, Case.GENITIVE, middlename)} '
                     f'(паспорт {pass_serie} {pass_number})', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    layout.add(Paragraph(f"Адрес: {address}", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # технический отступ
    layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # шрифт BOLD
    font_path_bold: Path = Path(__file__).parent / "Vollkorn-Bold.ttf"
    custom_font_bold: Font = TrueTypeFont.true_type_font_from_file(font_path_bold)

    # заголовок
    layout.add(Paragraph("ЗАЯВЛЕНИЕ ОБ ОТЗЫВЕ СОГЛАСИЯ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ", horizontal_alignment=Alignment.CENTERED, font=custom_font_bold, font_size=9))

    # технический отступ
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # первый абзац
    layout.add(Paragraph(f'***** ****, '
                     f'{maker.make(NamePart.LASTNAME, Gender.MALE, Case.INSTRUMENTAL, lastname)} '
                     f'{maker.make(NamePart.FIRSTNAME, Gender.MALE, Case.INSTRUMENTAL, firstname)} '
                     f'{maker.make(NamePart.MIDDLENAME, Gender.MALE, Case.INSTRUMENTAL, middlename)} '
                     f'({birth_date} года рождения, место рождения: {birth_place}, '
                     f'паспорт РФ: {pass_serie} №{pass_number}, код подразделения: {division_code}, выдан: {issue_date} г. ' 
                     f'{whom_issued}, '
                     f'зарегистрирован по адресу: {address}), '
                     f'* ****, {bank_name}{bank_data} '
                     f'{contract_date} **** ******** кредитный договор № {contract_number}. '
                     f'*** ********** ********** ******** **** *** ********* '
                     f'************ ****** *** *** ********* ************ '
                     f'****** **** **** ******** ** ********** **** '
                     f'************ ******."', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    #   второй абзац
    layout.add(Paragraph(f'******** ************ ****** ** * ****** "* '
                     f'************ ******", *** ********** ********** '
                     f'************ ****** **********, * *** *****, '
                     f'************* * ********* ******. ****** * ******* * '
                     f'********** ************ ****** *** **** ***** ******** '
                     f'* *** * ********* * **** *********** ***** '
                     f'*************** **** ***** ** ********* '
                     f'************ ******.', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # третий абзац
    layout.add(Paragraph(f'********* ***** ***** ** ************* ************ ****** ********: '
                     f'**** ********** ********* * ****** ****** *** *********, **** * ********* ************; '
                     f'****** ********** **** *************; '
                     f'****** * ************ ***** ************.', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # четвертый абзац
    layout.add(Paragraph(f'******* ********, *** ***** ***** ** ************* **** '
                     f'************ ****** * ********* ***** ** ******** **** '
                     f'***** *** ***** ******* ***, ********* ******** ** ** '
                     f'**** ***** ************ ***** ******** ***** * '
                     f'*********** *****. ***** ****, ** * **** ************** '
                     f'** ************ ***************** ****** ************ '
                     f'********** ********** ***********, *** **** *********** '
                     f'** ********** ******. ******* *********** ************** '
                     f'************ ************* ********* ************ '
                     f'******** ******. **** * *** ******* ** *** *********, '
                     f'** ** ** ****** ********* * ******** *******. ***** '
                     f'*******, ************* ************* **** ********* '
                     f'************ ****** * ********* ****** ******. ******* '
                     f'********, *** *** ********** ********** ******** **** '
                     f'** ******** ********** ** ******** **** ************ '
                     f'****** * ** ************* ******** ****** '
                     f'(************). *******, *** *** ********** ******** '
                     f'*** ************ * ****** ********** **** ** ****** '
                     f'*** ***** ** ************* ** ************ ******. * '
                     f'***** * ***, ***** ****** * ********* * **** ***** – '
                     f'************ * ******** ** *************** ********* '
                     f'* ************ **.', horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # пятый абзац
    layout.add(Paragraph(f'************ ********* * ******* *** * ********* * **** '
                     f'************, *** * ** ***** ***** ***** ************** '
                     f'******** **** ****, ******** **** ************* *** '
                     f'******** **** ************, *** ** *** ** ***** ***** '
                     f'************** **********, ********** ********** ***** '
                     f'* *********** ****** ******* *****. ******** *** * '
                     f'********* * **** ************ ***** ******* '
                     f'*************** * *********** ********** * **** '
                     f'**************, ** ****** ************** ********* * ***.', 
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # шестой абзац
    layout.add(Paragraph(f'************** ******* ** ** № ***-** «* ************ ******» *****: '
                     f'* ******* ********* ******* ********* ***** ********** '
                     f'********* **** *********** ****** * ********* *****; '
                     f'********* **** * *********** ************ ******* '
                     f'********* ********* * ******* ** **** * ******* *** '
                     f'*********. ***** ** ********* ***** ********* ** '
                     f'***** ** ****** ********** ****.',
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    # седьмой абзац
    layout.add(Paragraph(f'*********, *** * ****** *********** *** *** **** '
                     f'********** ***** ********** *******, *** *********'
                     f'– **** *********** ****** ******** *** ************* '
                     f'* ********* ****************** **** ******* *****. * '
                     f'******, **** ** ************ ******** *** ************ '
                     f'****** ******** ****, ****** **************** *********** '
                     f'**** **** *********** ** ****** ************ ****** * '
                     f'********* *********** ************, ********* * '
                     f'********** ************ **************** ** «* ************ '
                     f'******». * *********** ****** ** ****** *********, **** ***** '
                     f'******* ******: * *********** **, * ************ **, * ***, * '
                     f'*********** **** **.',
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))               

    # технические отступы
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))
    # layout.add(Paragraph(f"", horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))

    #  подпись
    layout.add(Paragraph(f'{lastname} {firstname} {middlename}',
                     horizontal_alignment=Alignment.LEFT, font=custom_font, font_size=9))             

    # store the PDF
    with open(Path(f"outputs/fakeoutputs/{id}.pdf"), "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)

