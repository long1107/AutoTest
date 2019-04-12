import xlrd

def readxls(x_name,t_name,x,y):
    xls = xlrd.open_workbook(x_name)
    table = xls.sheet_by_name(t_name)
    value = table.cell(x,y).value
    return value

val={
    "x_name":"data.xls",
    "t_name":"Sheet1",
    "x":0,
    "y":0
}