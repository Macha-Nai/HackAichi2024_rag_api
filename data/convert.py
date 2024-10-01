import csv
import uuid

# 入力ファイル名と出力ファイル名を指定
input_file = 'input.csv'
output_file = 'output.csv'

# 抽出したい列のヘッダー名をリスト化
columns_to_extract = ['管理NO', '問合せ内容', '回答内容']

# CSVファイルを読み込み、必要な列を抽出して新しいCSVに書き込む
with open(input_file, 'r', encoding='utf-8-sig') as infile:
    reader = csv.DictReader(infile)
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=columns_to_extract)
        writer.writeheader()
        for row in reader:
            # 管理NOに新しいUUIDを割り振る
            row['管理NO'] = str(uuid.uuid4())
            filtered_row = {key: row[key] for key in columns_to_extract}
            writer.writerow(filtered_row)
