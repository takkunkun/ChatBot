# 別ファイル
from speak import Bot, User
from test_class import test, test2

# メイン処理
if __name__ == "__main__":
    print('---チャットボットのテストをスタートします---')
    bot = Bot("B")
    user = User("U")
    bot.print("ボットです。")

    test2(bot.name, user.name)
    print()
    test()

    print('---チャットボットのテストが終了しました---')
