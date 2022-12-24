"""話すクラス"""
# 標準ライブラリ
import unicodedata

# 初期値
BotName = 'python'  # ボットの名前
UserName = 'you'  # ユーザーの名前

# ファイルに保存してあるユーザーネームを取得する。
try:
    f = open('username.txt', 'r', encoding='utf-8')
except OSError:
    pass
else:
    line = f.readline()
    # 改行コードが在ったら空白にする。
    line = line.replace('\n', '')
    UserName = line
    f.close()


def len_str(str: str) -> int:
    """
    文字数をカウントする。
    半角は1
    全角は2
    """
    count = 0
    for c in str:
        if unicodedata.east_asian_width(c) in ('F', 'W', 'A'):
            count += 2
        else:
            count += 1
    return count


len_BotName = len_str(BotName)
len_UserName = len_str(UserName)


class speak:
    """話すクラス"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def bot(speak: str) -> None:
        print('{} > {}'.format(BotName, speak))

    @staticmethod
    def user(speak: str) -> None:
        print('{} > {}'.format(UserName, speak))


# メイン処理
if __name__ == "__main__":
    obj = speak()
    obj.bot("ボットです。")
    obj.user("ユーザーです。")

    speak.bot("あ")
