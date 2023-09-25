import openpyxl
from openpyxl.cell import MergedCell
from openpyxl.utils.cell import get_column_letter

book = openpyxl.load_workbook('./data/timetable_april.xlsx')

print('Введите день, на которое вы хотите узнать расписание\n')
number = int(input())
#number = 21

if int(number) < 9:
    number += 1
elif int(number) >= 15:
    number -= 1

print("Напишите название класса в котором вы учитесь")
your_class = input()
#your_class = '8А'

sheet = book.worksheets[number]
# sheet = book['17']
number_rows = sheet.max_row
number_columns = sheet.max_column


def get_merged_cell_value(sheet, cell):
    rng = [s for s in sheet.merged_cells.ranges if cell.coordinate in s]
    return sheet.cell(rng[0].min_row, rng[0].min_col).value if len(rng) != 0 else cell.value


def find_class_cell(value):
    for i in range(number_columns):
        for k in range(number_rows):
            cell = sheet[get_column_letter(i + 1) + str(k + 1)]
            if cell.value and value in str(cell.value):
                return (cell.column, cell.row)


def find_count_of_subjects(class_cell):
    count = 0
    for i in range(1, 20):
        if sheet.cell(column=class_cell[0], row=class_cell[1] + i).value is None and count != 0:
            break
        count += 1
    return count


def find_serial_numbers(class_cell):
    count = 0
    serial_numbers = []
    for i in range(1, 20):
        if sheet.cell(column=2, row=class_cell[1] + i).value is None and count != 0:
            break

        count += 1
        serial_numbers.append(count)

    return tuple(serial_numbers)


def find_time_cells(class_cell):
    time_cells = []
    for i in range(1, 20):
        time_cells.append(sheet.cell(column=3, row=class_cell[1] + i).value)
        if sheet.cell(column=3, row=class_cell[1] + i).value is None:
            break
    return tuple(time_cells)


def find_class_subjects(class_cell):
    subjects = []
    for i in range(1, find_count_of_subjects(class_cell) + 1):
        cell = sheet.cell(column=class_cell[0], row=class_cell[1] + i)
        if isinstance(cell, MergedCell):
            # print(get_merged_cell_value(sheet, cell))
            subjects.append(get_merged_cell_value(sheet, cell))
        else:
            # print(cell.value)
            subjects.append(cell.value)
    return tuple(subjects)


def create_a_schedule(class_cell):
    return zip(find_serial_numbers(class_cell), find_time_cells(class_cell), find_class_subjects(class_cell))


cell = find_class_cell(your_class)

# answer = create_a_schedule(cell)
for answer in create_a_schedule(cell):
    print(f'№{answer[0]} Time: {answer[1]} Subject: {answer[2]}')
