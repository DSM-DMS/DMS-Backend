def get_cells(student):
    number = student.number

    # Get row
    grade = int(number / 1000)
    if grade == 1:
        row_start = 3
    elif grade == 2:
        row_start = 26
    else:
        row_start = 48
    row = row_start + number % 100 - 1

    # Get cols
    class_ = int(number % 1000 / 100)
    number_col = chr(ord('B') + (class_ - 1) * 4)
    name_col = chr(ord(number_col) + 1)
    status_col = chr(ord(name_col) + 1)

    # Get cells
    number_cell = number_col + str(row)
    name_cell = name_col + str(row)
    status_cell = status_col + str(row)

    return number_cell, name_cell, status_cell
