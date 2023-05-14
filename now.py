# 作成開始日：2023/05/14
# 現在作成途中
"""
現在の日付と時刻を表示する。
例）「2023年5月14日日曜日0時0分0秒」
"""
import datetime
def get():
    # 曜日リスト
    days: list[str] = ['月', '火', '水', '木', '金', '土', '日']

    today = datetime.date.today()
    now = datetime.datetime.now().time()

    # 年
    year :int = today.year
    # 月
    month :int = today.month
    # 日
    day :int = today.day
    # 曜日
    weekday: str = days[datetime.date.today().weekday()]
    # 時
    hour: int = now.hour
    # 分
    minute: int = now.minute
    # 秒
    second: int = now.second



if __name__ == "__main__":
    print(f"{year}年{month}月{day}日{weekday}曜日{hour}時{minute}分{second}秒")
    # print(f"{year}/{month}/{day}({weekday}) {hour}:{minute}:{second}")

