"""
チャットボット
第3回効果測定のやつを作り直す
python3.10で作成
"""
# 標準ライブラリ
from datetime import datetime
import random

# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary


class command:
    def select() -> int:
        """コマンド(したいこと)を選択。"""
        ans = questionary.select(
            '何をする？',
            # choices=command_list,
            choices=[
                questionary.Choice(title="曜日当てゲーム", value=1),
            ],
            use_shortcuts=True,
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")
        command.do(ans)

    def do(num: int) -> None:
        match num:
            case 1:
                obj: object = today()
                obj.do()
            case _:
                print("この番号は存在しません。")


class today():
    def __init__(self) -> None:
        print("曜日当てゲームをします。")

    days = ['月', '火', '水', '木', '金', '土', '日']
    today = datetime.now().weekday()
    day = days[today]

    def do(self):
        ans_day = questionary.select(
            '今日は何曜日？',
            choices=self.days,
            use_shortcuts=True,
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")

        # キャンセルの場合、「None」が返ってくる
        if not(ans_day == None):
            if(ans_day == self.day):
                print("正解")
            else:
                print("不正解")
                print(f"正解は、「{self.day}」でした。")


print('---チャットボットをスタートします---')
print()
command.select()
print()
print('---チャットボットが終了しました---')
