import openpyxl

wb = openpyxl.load_workbook("ceu.xlsx")
ws = wb.active

targetList = []

for row in ws.iter_rows(min_row=1, max_col=1, max_row=310):
    for cell in row:
        print(f"Adding {cell.value}")
        targetList.append(cell.value)

print(targetList)