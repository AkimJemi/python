from openpyxl import load_workbook
import Util as u
dbFileName = "db/db.xlsx"
pyName = "repositoryLT"

u.showLog(__file__, None, None)


def sheetAutoCheckAndInsert(info, sheetName, num):
    wb = load_workbook(dbFileName)
    ws = wb.active
    ws_names = wb.sheetnames
    sheet = None
    for a_sheet in ws_names:
        if a_sheet == sheetName:
            sheet = wb.get_sheet_by_name(sheetName)

    if sheet == None:
        wb.create_sheet(sheetName)
        sheet = wb[sheetName]

    max_row = sheet.max_row
    if sheet['A1'].value == None and max_row == 1:
        max_row = 1
    elif sheet['A1'].value != None and max_row == 1:
        max_row = 2
    else:
        max_row = max_row + 1

    sheet.cell(row=max_row, column=1).value = max_row
    for i in range(2, num+2):
        sheet.cell(row=max_row, column=i).value = info[i-2]
    wb.save(dbFileName)


def getUserList():
    print(pyName+"getUserList")
    import Util
    sheetName = Util.sheetnames[1]
    wb = load_workbook(filename=dbFileName, data_only=True)
    ws = wb[sheetName]
    userList = []
    for y in range(1, ws.max_row+1):
        userList.append(ws.cell(column=2, row=y).value)

    return userList


def saveGameMatchTeamSetting(info):
    import Util
    sheetName = Util.sheetnames[0]
    print(pyName+sheetName)
    sheetAutoCheckAndInsert(info, sheetName, 5)


def saveUserInfo(info):
    import Util
    sheetName = Util.sheetnames[1]
    print(pyName+sheetName)
    sheetAutoCheckAndInsert(info, sheetName, 3)
    from mainPage import setUserList
