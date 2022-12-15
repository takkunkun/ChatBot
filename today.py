"""今日の曜日を当てる"""
# 標準ライブラリ
from datetime import datetime

# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary

days = ['月', '火', '水', '木', '金', '土', '日']

today = datetime.now().weekday()
day = days[today]

ans_day = questionary.select(
    '今日は何曜日？',
    choices=days,
    use_shortcuts=True,
    use_jk_keys=False,
    instruction="（数字キーまたは矢印キーを使用）"
).ask(kbi_msg="キャンセルされました。")

# キャンセルの場合、「None」が返ってくる
if not(ans_day == None):
    if(ans_day == day):
        print("正解")
    else:
        print("不正解")
        print(f"正解は、「{day}」でした。")
