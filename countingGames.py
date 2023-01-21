# 更新日：2023/01/10
# 作成日：2023/01/06

# 標準ライブラリ
import random
from typing import Any

# 外部ライブラリ
from colorama import Back, Fore, Style, init
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary
from questionary import Validator, ValidationError

# 別ファイル
import speak as s
from speak import speak

# 文字色を自動で元に戻す
init(autoreset=True)

UserName = s.UserName


class NumValidator(Validator):
    def __init__(self, min: int, max: int) -> None:
        self.min = min
        self.max = max

    def validate(self, document: Any) -> None:
        text = document.text
        if len(text) == 0:
            raise ValidationError(
                message="値を入力してください。",
                cursor_position=len(text),
            )
        try:
            text = int(text)
        except ValueError:
            raise ValidationError(
                message="数値以外が入力されています。",
            )
        if (text < self.min) or (self.max < text):
            raise ValidationError(
                message=f"{self.min}以上{self.max}以下で入力してください。",
            )


class countingGames():
    """数当てゲームクラス"""

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
            ans = questionary.text(
                "",
                qmark=(f"{UserName} >"),
                validate=NumValidator(min, max)
            ).ask(kbi_msg="キャンセルされました。")
            if ans is None:
                # questionaryで「KeyboardInterrupt」の場合、Noneが返ってくる
                break
            ans = int(ans)
            count += 1
            if ans == num:
                speak.bot(Fore.LIGHTMAGENTA_EX + "正解です。")
                speak.bot2(f"{UserName}さんは、" + Style.BRIGHT +
                           f"{count}回" + Style.RESET_ALL + "で正解しました。")
                break
            elif ans < num:
                speak.bot("もっと大きい数です。")
            elif ans > num:
                speak.bot("もっと小さい数です。")
            if (num - num_hint <= ans <= num + num_hint):
                speak.bot2("惜しい。")
        speak.bot("数当てゲームを終わります。")


# メイン処理
if __name__ == "__main__":
    obj = countingGames()
    obj.do()
