# 更新日：2023/01/03
# 作成日：2022/12/29

# 標準ライブラリ
import unicodedata

# 外部ライブラリ
from colorama import Back, Fore, Style, init

init(autoreset=True)

# 初期値
BotName = "python"  # ボットの名前
UserName = "you"  # ユーザーの名前


def get_username() -> (str):
    """ファイルに保存してあるユーザーネームを取得する。"""
    try:
        f = open("username.txt", "r", encoding="utf-8")
    except OSError:
        UserName = ""
    else:
        line = f.readline()
        # 改行コードが在ったら空白にする。
        line = line.replace("\n", "")
        UserName = line
        f.close()
    return UserName


def len_str(str: str) -> int:
    """
    文字数をカウントする。
    半角は1
    全角は2
    """
    count = 0
    for c in str:
        if unicodedata.east_asian_width(c) in ("F", "W", "A"):
            count += 2
        else:
            count += 1
    return count


UN = get_username()
if UN != "":
    UserName = UN

del UN

len_BotName = len_str(BotName)
len_UserName = len_str(UserName)


class speak:
    """話すクラス"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def bot(speak: str) -> None:
        """ボットが話す1行目関数"""
        print("{} > {}".format(BotName, speak))

    @staticmethod
    def bot2(speak: str) -> None:
        """ボットが話す2行目以降関数"""
        print("%{}s  %s".format(len_BotName + 1) %
              ("", speak))

    @staticmethod
    def bot_error(speak: str) -> None:
        """ボットが話す1行目関数(文字色赤)"""
        print("{} > ".format(BotName) + Style.BRIGHT +
              Fore.RED + "{}".format(speak))

    @staticmethod
    def bot2_error(speak: str) -> None:
        """ボットが話す2行目以降関数(文字色赤)"""
        print(Style.BRIGHT +
              Fore.RED + "%{}s  %s".format(len_BotName + 1) %
              ("", speak))

    @ staticmethod
    def user(speak: str) -> None:
        """ユーザーが話す1行目関数"""
        print("{} > {}".format(UserName, speak))

    @ staticmethod
    def user2(speak: str) -> None:
        """ユーザーが話す2行目以降関数"""
        print("%{}s  %s".format(len_UserName + 1) %
              ("", speak))

    @ staticmethod
    def user_input(speak: str) -> str:
        """ユーザーに入力を求める関数"""
        return input("{} > {}".format(UserName, speak))


class get():
    """ゲッタークラス"""

    def __init__(self) -> None:
        pass

    @ staticmethod
    def botname() -> str:
        return BotName

    @ staticmethod
    def username() -> str:
        return UserName


# メイン処理
if __name__ == "__main__":
    print("-----表示テスト-----")
    obj = speak()
    obj.bot("ボットです。")
    obj.bot2("よろしく！")
    obj.bot_error("ボットエラー")
    obj.bot2_error("ボットエラー2")
    obj.user("ユーザーです。")
    obj.user2("よろしく！")
    print("-----表示テスト-----")
