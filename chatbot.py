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


class command:
    def select(self) -> None:
        """コマンド(したいこと)を選択。"""
        ans = questionary.select(
            '何をする？',
            choices=[
                questionary.Choice(title="曜日当てゲーム", value=1),
            ],
            use_shortcuts=True,
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")
        if ans is not None:
            self.do(ans)

    @staticmethod
    def do(num: int) -> None:
        command_list = ["", "today"]
        obj = eval(command_list[num])()
        obj.do()


class today():
    def __init__(self) -> None:
        print("曜日当てゲームをします。")

    days = ['月', '火', '水', '木', '金', '土', '日']
    # yyyy-mm-dd
    today = datetime.date.today()
    day = days[today.weekday()]

    def do(self) -> None:
        ans_day = questionary.select(
            '今日は何曜日？',
            choices=self.days,
            use_shortcuts=True,
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")

        # キャンセルの場合、「None」が返ってくる
        if ans_day is not None:
            if(ans_day == self.day):
                print("正解")
            else:
                print("不正解")
                print(f"正解は、「{self.day}」でした。")


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
