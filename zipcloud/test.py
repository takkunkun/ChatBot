import json
# ファイルを開く
with open("zipcloud_3350000.json", mode='r', encoding="utf-8") as f:
    # 取得したデータをjson形式でロードする。
    data = json.load(f)

for result in data["results"]:
    # print(f"{result["address1"]}{result["address2"]}{result["address3"]}")
    print("〒：{}".format(result["zipcode"]), end=" ")
    print("{}{}{}".format(result["address1"],
          result["address2"], result["address3"]))