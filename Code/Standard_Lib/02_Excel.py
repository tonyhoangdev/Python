#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : Excel
"""
import xlsxwriter

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook("test1.xlsx")
worksheet = workbook.add_worksheet("Test1")

# Widen the first column to make the text clearer
worksheet.set_column('A:A', 50)
worksheet.set_row(0, 40)


# Add a bold format to use to highlight cells
bold = workbook.add_format({'bold': True})
font = workbook.add_format({'font_size': 20})

# Write some simple text
worksheet.write('A1', 'Hello')

# Text with formatting
worksheet.write('A2', 'World', bold)

# Write some numbers with row/column notation
worksheet.write(2, 0, "'123", font)
worksheet.write(3, 0, 123.456)
worksheet.write(4, 0, 36)

# Close workbook
workbook.close()
