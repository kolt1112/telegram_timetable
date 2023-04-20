import openpyxl
from openpyxl.utils.cell import get_column_letter

wb = openpyxl.load_workbook('./data/timetable_april.xlsx')

sheet = wb['3']
number_rows = sheet.max_row
number_columns = sheet.max_column


def find_class_cell(value):
    for i in range(number_columns):
        for k in range(number_rows):
            cell = sheet[get_column_letter(i + 1) + str(k + 1)]
            if cell.value and value in str(cell.value):
                return cell.coordinate


# TODO: find all subjects bu class name
def find_class_subjects(class_cell):
    pass
