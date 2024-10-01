import csv
import requests
import json

# 入力CSVファイルの名前を指定
csv_file = './keyword.csv'

# POSTリクエストを送信するURLを指定
url = 'http://localhost:8889/v1/collections/my_collection/upsert/not_use_gpt'

# ヘッダー情報を指定
headers = {
    "Content-Type": "application/json"
}

# CSVファイルを読み込み、各行についてPOSTリクエストを送信
with open(csv_file, 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        id_value = row['管理NO']
        keyword = row['キーワード']

        payload = {
            "id": id_value,
            "metadata": {"key": "value"},
            "input": keyword,
            "use_gpt": False,
        }

        print(f"Upserting ID {id_value} with keyword {keyword}")

        # POSTリクエストを送信
        response = requests.post(url, headers=headers, json=payload)

        # レスポンスのステータスコードをチェック
        if response.status_code == 200:
            print(f"ID {id_value} was successfully upserted.")
        else:
            print(f"Failed to upsert ID {id_value}: {response.status_code}, {response.text}")
