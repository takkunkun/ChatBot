# 更新日：2023/01/04
# 作成日：2023/01/04

# 別ファイル
import speak as s
from speak import speak

BotName = s.BotName
UserName = s.UserName


class self_introduction():
    """自己紹介クラス"""

    def __init__(self) -> None:
        pass

    def do(self) -> None:
        """自己紹介本体"""
        speak.bot("自己紹介をします。")
        speak.bot("私の名前は{}です。".format(BotName))
        speak.bot("あなたの名前を教えてください。")
        YourName = speak.user_input("")
        speak.bot("あなたは{}さんですね。".format(YourName))
        speak.bot("よろしくお願いします。")
        # 名前をファイルに書き込む。
        f = open("username.txt", "w", encoding="utf-8")
        f.write(YourName)
        f.close()
        global UserName
        UserName = YourName


# メイン処理
if __name__ == "__main__":
    obj = self_introduction()
    obj.do()
    UserName = s.get_username()
    print(UserName)
