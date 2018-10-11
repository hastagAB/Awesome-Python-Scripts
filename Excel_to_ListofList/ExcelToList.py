import xlrd
import sys

class ExcelToList():

	def __init__(self, file, sheet):
		self.file = file
		self.sheet = sheet

	def convert(self):
		converted_list = []
		inputexcel = xlrd.open_workbook(self.file)
		inputsheet = inputexcel.sheet_by_name(self.sheet)
		numberofrows = inputsheet.nrows
		numberofcols = inputsheet.ncols
		start_row,start_col = 0,0
		for current_row in range(start_row,numberofrows):
			currentlist = []
			for current_col in range(start_col,numberofcols):
				currentlist.append(inputsheet.cell(current_row,current_col).value)
			converted_list.append(currentlist)
		return converted_list