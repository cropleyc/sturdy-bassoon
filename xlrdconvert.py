import xlrd
import csv
 
with xlrd.open_workbook('Query (2).xls') as wb:
    sh = wb.sheet_by_index(0)  # wb.sheet_by_name('sheet_name')
    with open('new.csv', 'w', newline="") as f:
        col = csv.writer(f)
        for row in range(sh.nrows):
            col.writerow(sh.row_values(row))
