# 更新日：2022/01/04
# 作成日：2022/12/29

# 郵便番号検索API - zipcloud (http://zipcloud.ibsnet.co.jp/doc/api)

# 外部ライブラリ
import requests

# 別ファイル
from speak import speak


class zipcode():
    """郵便番号から住所を検索するクラス"""

    def __init__(self) -> None:
        pass

    def do(self) -> None:
        """郵便番号から住所を検索する"""
        speak.bot("郵便番号から住所を検索します。")
        speak.bot("郵便番号を入力してください。")
        while True:
            # 郵便番号を入力させる。
            zipcode = input("〒：")
            try:
                # データを取得する。
                request_data = requests.get(
                    'https://zipcloud.ibsnet.co.jp/api/search?zipcode={}&limit=100'
                    .format(zipcode))
            except requests.exceptions.ConnectionError:
                speak.bot_error("取得できませんでした。")
                speak.bot2_error("インターネット接続などを確認してください。")
                break
            except Exception as e:
                # https://srbrnote.work/archives/5125
                print(e.__class__.__name__)
                import traceback
                print(traceback.format_exc())
                break
            else:
                # 取得したデータをjson形式でロードする。
                data = request_data.json()
                # データが正常に受け取れた時
                if data["status"] == 200:
                    results = data['results']
                    # nullではない時
                    if results:
                        result_len = len(results)
                        print(f"{result_len}件見つかりました。")
                        # 住所を表示する。
                        for result in results:
                            print("住所：{}{}{}".format(result["address1"],
                                                     result["address2"], result["address3"]))
                        break
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
            speak.bot2("もう一度郵便番号を入力してください。")


# メイン処理
if __name__ == "__main__":
    obj = zipcode()
    obj.do()
