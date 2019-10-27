from urllib import request
from bs4 import BeautifulSoup
import re
import copy
import time
import datetime
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
TARGET_LINE_ID = os.getenv('TARGET_LINE_ID', None)
LINE_BOT_API = LineBotApi(CHANNEL_ACCESS_TOKEN)


def scraping():
    # url
    url = "https://atcoder.jp/contests/"
    wait_hours = 12
    wait_seconds = wait_hours * 3600
    content_L_old = []

    while True:
        try:
            content_L = []

            # set BueatifulSoup & extract tags
            html = request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            parsed = soup.find_all(
                "div", attrs={"id": "contest-table-upcoming"})

            # extract time and contest info by using regex
            data = str(parsed[0])
            search_result_time = re.findall(
                r"<time class=\"fixtime fixtime-full\".+>", data)
            search_result_content = re.findall(r"<a href=\"\/contests.+", data)
            for t, c in zip(search_result_time, search_result_content):
                content = c.replace("<", ">").split(">")[2]
                date_time = t.replace("<", ">").split(">")[2]
                content_L.append((content, date_time))
                today = str(datetime.date.today())

                # today's contest judge
                if today == date_time[:10]:
                    line_message = "本日（{0}） {1}があります".format(
                        date_time, content)
                    print(line_message)
                    push_massage(line_message)

            # new content judge
            if len(content_L_old) < len(content_L):
                new_content_num = len(content_L_old) - len(content_L)
                for _num in range(new_content_num, 0):
                    line_message = "新しいコンテストが追加されました\n {0} \n {1}".format(
                        content_L[_num][0], content_L[_num][1])
                    print(line_message)
                    push_massage(line_message)
            content_L_old = copy.copy(content_L)

        # error handling
        except:
            line_message = "エラー発生. something is wrong"
            push_massage(line_message)
            time.sleep(10)

        time.sleep(wait_seconds)


def push_massage(line_message):
    LINE_BOT_API.push_message(
        TARGET_LINE_ID, TextSendMessage(text=line_message))


if __name__ == "__main__":
    scraping()
