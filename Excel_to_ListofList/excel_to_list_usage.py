from ExcelToList import ExcelToList

exceltolist = ExcelToList("input.xlsx","Sheet1") ## args : Input filename, Sheet name
list_of_list = exceltolist.convert()

print "List of List : ",list_of_list