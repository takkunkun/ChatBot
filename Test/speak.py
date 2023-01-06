# 更新日：2023/01/06
# 改修日：2023/01/06
# 作成日：2022/12/29

# 標準ライブラリ
import unicodedata
from typing import Any

# 外部ライブラリ
from colorama import Back, Fore, Style, init

init(autoreset=True)


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


class Person:
    """クラス"""

    def __init__(self, name: str = "Python") -> None:
        """コンストラクター"""
        self.__name = name  # の名前
        self.__len = len_str(self.__name)  # 名前の長さ

    @property
    def name(self) -> str:
        """名前を取得（ゲッター）"""
        return self.__name

    @name.setter
    def name(self, name: Any) -> None:
        """名前を設定（セッター）"""
        if name is None:
            raise TypeError('invalid name')
        self.__name = name

    @property
    def len(self) -> int:
        """名前の長さ取得（ゲッター）"""
        return self.__len

    @len.setter
    def len(self, len: int) -> None:
        """名前の長さを設定（セッター）"""
        self.__len = len

    def print(self, speak: str) -> None:
        """話す1行目関数"""
        print(f"{self.name} > {speak}")

    def print2(self, speak: str) -> None:
        """話す2行目以降関数"""
        print("%{}s  %s".format(self.len + 1) %
              ("", speak))


class Bot(Person):
    """ボットクラス"""

    def __init__(self, name: str = "Python") -> None:
        super().__init__(name)

    def error(self, speak: str) -> None:
        """ボットが話す1行目関数(文字色赤)"""
        print("{} > ".format(self.name) + Style.BRIGHT +
              Fore.RED + "{}".format(speak))

    def error2(self, speak: str) -> None:
        """ボットが話す2行目以降関数(文字色赤)"""
        print(Style.BRIGHT +
              Fore.RED + "%{}s  %s".format(self.len + 1) % ("", speak))


class User(Person):
    """ユーザークラス"""

    def __init__(self, name: str = "you") -> None:
        super().__init__(name)
        self.get_username()

    def get_username(self) -> None:
        """ファイルに保存してある名前を設定"""
        try:
            f = open("username.txt", "r", encoding="utf-8")
        except OSError:
            pass
        else:
            line = f.readline()
            # 改行コードが在ったら空白にする。
            line = line.replace("\n", "")
            # ユーザー名を設定
            self.name = line
            # ユーザー名の長さを設定
            self.len = len_str(line)
            f.close()

    def input(self, speak: str) -> str:
        """ユーザーに入力を求める関数"""
        return input(f"{self.__name} > {speak}")


# メイン処理
if __name__ == "__main__":
    print("-----表示テスト-----")
    bot = Bot()
    bot.print("ボットです。")
    bot.print2("よろしく！")
    bot.error("ボットエラー")
    bot.error2("ボットエラー2")

    user = User()
    user.print("ユーザーです。")
    user.print2("よろしく！")
    print()
    bot = Bot("B")
    bot.print(f"{bot.name}です。")
    bot.print2("よろしく！")
    user = User("U")
    user.print(f"{user.name}です。")
    user.print2("よろしく！")

    print("-----表示テスト-----", end="")
