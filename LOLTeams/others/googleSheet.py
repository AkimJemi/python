import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'C:/Users/wowp1/Desktop/laptop_github/laptop_repository/python/LOLTeams/src/key.json', scope)
client = gspread.authorize(creds)

doc = client.open_by_url(
    'https://docs.google.com/spreadsheets/d/1acywHAwyLtUH4uA_OR1ZtA31BoH09ofdxZTi-1BOIrA/edit?pli=1#gid=0')

sheet1 = doc.worksheet('11')


cnt = int(sheet1.cell(1, 2).value)
print('기존 행수 : ', cnt)

sheet1.insert_row(['지마켓', '사탕', '022'])
sheet1.update_cell(1, 2, str(cnt+1))
