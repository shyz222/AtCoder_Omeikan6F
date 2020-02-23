""""
日経新聞のHPに一時間ごとに日経平均株価を見に行き
平均株価を表示しCSVファイルに出力
"""

import requests
from bs4 import BeautifulSoup
import datetime
import jpholiday
import csv
import time

url = "http://www.nikkei.com/markets/kabu/"

response = requests.get(url)

while True:
    if datetime.datetime.now().minute != 59:
        time.sleep(58)
        continue
    
    #ファイルオープン
    f = open('nikkei_heikin_ver2.csv', 'a')
    writer = csv.writer(f, lineterminator='\n')

    # 59分になっても正確な時間を測定するために秒間隔で59秒になるまで出ない
    while datetime.datetime.now().second != 59:
        time.sleep(1)
    
    time.sleep(1)

    #CSVのレコード作成
    csv_list = []

    # 現在の時刻を年、月、日、時、分、秒で取得
    time_ = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    #リストの一カラム目に現在時刻を追加
    csv_list.append(time_)

    #文字化け防止
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")

    span = soup.find_all("span")

    #printのエラー防止
    nikkei_heikin_kabu = ""
    nikkei_heikin_zenjituhi = ""

    for tag in span:
        try:
            #spanタグの中からclass='mkc-stock-prices'であるものを探索
            nikkei_heikin = soup.find('span', class_='mkc-stock_prices')
            #spanタグの中からclass='cmn-minus'であるものを探索
            nikkei_heikin_ = soup.find('span', class_='cmn-minus')

            nikkei_heikin_kabu = nikkei_heikin.text
            nikkei_heikin_zenjituhi = nikkei_heikin_.text
    
        except:
            print('Error')
            break

    #日経平均株価を表示
    print(time_, nikkei_heikin_kabu, nikkei_heikin_zenjituhi)

    #2カラム目に日経平均株価を追加
    csv_list.append(nikkei_heikin_kabu)

    csv_list.append(nikkei_heikin_zenjituhi)

    # csvに追記
    writer.writerow(csv_list)

    # ファイル破損防止
    f.close()