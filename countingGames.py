# 更新日：2023/01/06
# 作成日：2023/01/06

# 標準ライブラリ
import random

# 外部ライブラリ
from colorama import Back, Fore, Style, init

# 別ファイル
import speak as s
from speak import speak

# 文字色を自動で元に戻す
init(autoreset=True)

UserName = s.UserName


class countingGames():
    def __init__(self) -> None:
        pass

    def do(self) -> None:
        speak.bot("数当てゲームを始めます")
        count: int = 0
        max: int = 999  # 当てる数の最大値
        min: int = 0  # 当てる数の最小値
        num: int = random.randint(min, max)  # 当てる数
        num_hint: int = 10  # ヒントの許容範囲±
        speak.bot(f"{min}から{max}の数字を当ててください。")

        while True:
            ans: int
            try:
                ans = int(speak.user_input(""))
            except ValueError:
                speak.bot_error("数字以外の文字が含まれています。")
                speak.bot2("もう一度入力してください。")
            else:
                count += 1
                if ans == num:
                    speak.bot(Fore.LIGHTMAGENTA_EX + "正解です。")
                    speak.bot2(f"{UserName}さんは、{count}回で正解しました。")
                    break
                elif ans < num:
                    speak.bot("もっと大きい数です。")
                elif ans > num:
                    speak.bot("もっと小さい数です。")
                # if and ((num - num_hint < ans), (ans < num + num_hint)):
                if (num - num_hint < ans) and (ans < num + num_hint):
                    speak.bot2("惜しい。")
        speak.bot("数当てゲームを終わります。")


# メイン処理
if __name__ == "__main__":
    obj = countingGames()
    obj.do()
