# 更新日：2022/01/04
"""
チャットボット
第3回効果測定のやつを作り直す
python3.10で作成
"""
# 標準ライブラリ
from typing import Any
from time import sleep

# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary
# 文字色を変えるライブラリ
from colorama import Back, Fore, Style, init

# 別ファイル
from RockScissorsPaper import RockScissorsPaper
from today import today
from zipcode import zipcode
from speak import speak
from self_introduction import self_introduction

# 文字色を自動で元に戻す
init(autoreset=True)


class command:
    def select(self) -> None:
        """コマンド(したいこと)を選択。"""
        ans = questionary.select(
            '何をする？',
            choices=[
                questionary.Choice(title="自己紹介", value=1),
                questionary.Choice(title="曜日当てゲーム", value=2),
                questionary.Choice(title="じゃんけんゲーム", value=3),
                questionary.Choice(title="郵便番号から住所検索", value=4),
            ],
            # 数字キーまたは矢印キーで選択できるようにする。
            use_shortcuts=True,
            # JKキーで選択できないようにする。
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")
        if ans is not None:
            self.do(ans)

    def do(self, num: int) -> None:
        """コマンド実行"""
        obj: Any
        match num:
            case 0:
                pass
            case 1:
                obj = self_introduction()
                obj.do()
            case 2:
                obj = today()
                obj.do()
            case 3:
                obj = RockScissorsPaper()
                obj.do()
            case 4:
                obj = zipcode()
                obj.do()
            case _:
                print("このコマンドは存在しません。")


def bool() -> Any:
    is_bool = questionary.confirm(
        "続けますか？",
        default=True,
    ).ask(kbi_msg="キャンセルされました。")
    # boolかNoneが返る！
    return is_bool


# メイン処理
print('---チャットボットをスタートします---')

while True:
    try:
        print()
        c = command()
        c.select()
        sleep(1)
        is_bool = bool()
        if any([is_bool is False, is_bool is None]):
            break
    except KeyboardInterrupt:
        speak.user2(Back.LIGHTBLUE_EX + Fore.BLACK + "'Ctrl + C'で停止しました。")
        break
print()
print('---チャットボットが終了しました---')
