# 別ファイル
from speak import Bot, User
from test import bot, user

class test:
    def __init__(self) -> None:
        bot.print(user.name)


class test2:
    def __init__(self, bot: str, user: str) -> None:
        """コンストラクター"""
        self.bot = Bot(bot)
        self.user = User()
        self.bot.print("１行目")
        self.bot.print2("２行目")
        print()
