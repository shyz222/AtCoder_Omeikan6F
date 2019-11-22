# 概要
Atcoderからコンテスト情報を取得し、任意の時間ごとにlineグループへコンテスト情報を送信する

# セットアップ手順
## 手順
- 各種環境変数取得
以下のコマンドを実行する
```

export LINE_CHANNEL_SECRET=1c***************************
export LINE_CHANNEL_ACCESS_TOKEN=oj*********************************
export TARGET_LINE_ID=C4*******************
```

LINE_CHANNEL_SECRET:lineのチャンネルシークレット

LINE_CHANNNEL_ACCESS_TOKEN:ラインのアクセストークン

TARGET_LINE_ID：グループもしくは個人のLine id。ただし、この取得は少し特殊。



- 実行
```
nohup python3 line_bot.py &
```

## TARGET_LINE_IDの取得方法
下記URL参照
https://www.pnkts.net/2018/06/03/line-messaging-api/


