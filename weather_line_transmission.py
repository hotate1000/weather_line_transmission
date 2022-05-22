import requests
import json
import acc_token  # 別ファイルでLineのトークンを管理する


# テキストを取得する
def get_weather(day_list):
    send_txt = ""
    for i in day_list:
        date_text = '\n' + "日付：" + data["319"][i]["date"] + '\n'
        weather_forecast = "天気予報：" + data["319"][i]["forecast"] + '\n'
        lowest_and_highest_temperature = "気温：" + \
            data["319"][i]["mintemp"].replace('-', '不明') + "～" + \
            data["319"][i]["maxtemp"].replace('-', '不明') + '\n'
        weather_details = "詳細：" + data["319"][i]["weathers"] + "\n"
        send_txt += date_text + \
            weather_forecast + \
            lowest_and_highest_temperature + \
            weather_details
    return send_txt


# ラインを送信する
def send_line(send_txt):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token.token}
    payload = {'message': send_txt}
    requests.post(url, headers=headers, params=payload)


if __name__ == "__main__":
    url = requests.get('https://api.aoikujira.com/tenki/week.php?fmt=json&city=319')
    data = json.loads(url.text)
    day_list = [0, 1]  # 当日が0, 次の日が1となる
    send_txt = (get_weather(day_list))
    send_line(send_txt)
