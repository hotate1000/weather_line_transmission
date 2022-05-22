# weather_line_transmission
任意の時間に今日と明日の天気情報をラインに送信するアプリです。
送信時間はコードで管理しておらず、タスクスケジューラで行うことを想定しています。

# 作成経緯
自分があまり天気を調べずに外に出るので、特定の時間に天気情報をラインに送信するようにしました。

# インストールが必要な外部ライブラリ
- [requests](https://docs.python-requests.org/en/latest/)（2022/05/22参照）
    - ライセンス：[Apache License 2.0](https://github.com/psf/requests/blob/main/LICENSE)

# 利用方法
- PythonからLineを送信するため[LINE Notify](https://notify-bot.line.me/ja/)（2022/05/22参照）にてトークンを発行します。
- ``weather_line_transmission.py``と同じディレクトに``acc_token.py``ファイルを作成します。
- ``acc_token.py``に``token``という名前の変数を作成します。
- ``token``変数の値はLINE Notifyで発行したトークンとします。
- タスクスケジューラ(Windows)で``weather_line_transmission.py``を定期処理するように設定します。
