from openpyxl import load_workbook
dbFileName = "db/db.xlsx"
pyName = "repositoryLT"


def saveUserInfo(info):
    print(pyName+".saveUserInfo")
    wb = load_workbook(dbFileName)
    ws = wb.active
    print(wb.get_sheet_by_name("UserInfo").max_row)
    print(wb.get_sheet_by_name("UserInfo").max_column)
    sheet2 = wb.get_sheet_by_name("UserInfo")

    max_row = sheet2.max_row
    print(sheet2.max_row)
    if sheet2['A1'].value != None and max_row == 1:
        max_row = 2

    print(max_row)
    sheet2.cell(row=max_row+1, column=1).value = max_row
    for i in range(2, 5):
        sheet2.cell(row=max_row+1, column=i).value = info[i-2]

    wb.save(dbFileName)


def getUserList():
    print(pyName+"getUserList")
    wb = load_workbook(filename=dbFileName, data_only=True)
    ws = wb.active
    userList = []
    for y in range(1, ws.max_row+1):
        userList.append(ws.cell(column=2, row=y).value)

    return userList


def saveGameMatchTeamSetting(info):
    print(pyName+"saveGameMatchTeamSetting")
    wb = load_workbook(filename=dbFileName, data_only=True)
    ws = wb.active
    sheet2 = wb["GameMatchTeamSetting"]
    max_row = sheet2.max_row
    if sheet2['A1'].value == None and max_row == 1:
        max_row = 1
    elif sheet2['A1'].value != None and max_row == 1:
        max_row = 2
    else:
        max_row = max_row + 1

    sheet2.cell(row=max_row, column=1).value = max_row
    for i in range(2, 7):
        sheet2.cell(row=max_row, column=i).value = info[i-2].get()

    wb.save(dbFileName)
