# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
# import questionary
import requests
# 別ファイル
from speak import speak


class zipcode():
    """郵便番号から住所を検索するクラス"""

    def __init__(self) -> None:
        speak.bot("郵便番号から住所を検索します。")

    def do(self) -> None:
        """郵便番号から住所を検索する"""
        speak.bot("郵便番号を入力してください。")
        # 郵便番号を入力させる。
        zipcode = input("〒：")
        try:
            # データを取得する。
            request_data = requests.get(
                'https://zipcloud.ibsnet.co.jp/api/search?zipcode={}'
                .format(zipcode))
            # 取得したデータをjson形式でロードする。
            data = request_data.json()
            # データが正常に受け取れた時
            if data["status"] == 200:
                if data['results'] is not None:
                    # 住所を表示する。
                    for result in data["results"]:
                        print("住所：{}{}{}".format(result["address1"],
                                                 result["address2"], result["address3"]))
                elif data['results'] is None:
                    speak.bot_error("該当する住所がありません。")
                    speak.bot2_error("郵便番号を確認してください。")
            elif data['status'] == 400:
                # 入力パラメータエラーだった場合。
                error_list = {
                    'パラメータ「郵便番号」の桁数が不正です。': '郵便番号の桁数を確認してください。',
                    '必須パラメータが指定されていません。': '郵便番号を入力してください。',
                    'パラメータ「郵便番号」に数字以外の文字が指定されています。': '郵便番号に数字以外の文字が含まれています。'
                }
                message = data['message']
                if message in error_list:
                    speak.bot_error(error_list[message])
        except Exception as e:
            print(e.__class__.__name__)
            import traceback
            print(traceback.format_exc())
        except requests.exceptions.ConnectionError:
            speak.bot_error("取得できませんでした。")


# メイン処理
if __name__ == "__main__":
    obj = zipcode()
    obj.do()
