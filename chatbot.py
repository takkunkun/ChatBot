"""
チャットボット
第3回効果測定のやつを作り直す
python3.10で作成
"""
# 標準ライブラリ
import datetime
import random

# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary

from RockScissorsPaper import RockScissorsPaper
from today import today


class command:
    def select(self) -> None:
        """コマンド(したいこと)を選択。"""
        ans = questionary.select(
            '何をする？',
            choices=[
                questionary.Choice(title="曜日当てゲーム", value=1),
                questionary.Choice(title="じゃんけんゲーム", value=2),
            ],
            use_shortcuts=True,
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")
        if ans is not None:
            self.do(ans)

    @staticmethod
    def do(num: int) -> None:
        command_list = ["", "today", "RockScissorsPaper"]
        obj = eval(command_list[num])()
        obj.do()


def bool():
    is_bool = questionary.confirm(
        "続けますか？",
        default=True,
    ).ask(kbi_msg="キャンセルされました。")
    return is_bool


# メイン処理
print('---チャットボットをスタートします---')

while True:
    print()
    c = command()
    c.select()
    is_bool = bool()
    print()
    if any([is_bool is False, is_bool is None]):
        break
print('---チャットボットが終了しました---')
