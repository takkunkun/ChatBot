"""今日の曜日を当てる"""
# 標準ライブラリ
import datetime

# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary


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

# メイン処理
if __name__ == "__main__":
    obj = today()
    obj.do()
