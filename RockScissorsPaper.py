# 標準ライブラリ
import random
from time import sleep

# 外部ライブラリ
# https://qiita.com/skokado/items/50861b95b236068fd7b9
# https://questionary.readthedocs.io/en/stable/index.html
import questionary


class RockScissorsPaper():
    """じゃんけんクラス"""
    hands = ("グー", "チョキ", "パー")
    decision = ("引き分け", "負け", "勝ち")

    def __init__(self):
        print("じゃんけんゲームを始めます。")

    def do(self):
        """じゃんけん本体"""
        # ユーザーにどの手を出すか選択させる。
        user_hond = questionary.select(
            'どの手を出す？',
            choices=[
                questionary.Choice(title="グー", value=0),
                questionary.Choice(title="チョキ", value=1),
                questionary.Choice(title="パー", value=2),
            ],
            use_shortcuts=True,
            use_jk_keys=False,
            instruction="（数字キーまたは矢印キーを使用）"
        ).ask(kbi_msg="キャンセルされました。")

        if user_hond is not None:
            # ボットの出す手をランダムにする。
            bot_hand = random.randint(0, 2)
            # 結果を求める。
            judge = (user_hond - bot_hand + 3) % 3

            # じゃんけんの結果を表示する。
            print("ジャン、", end='', flush=True)
            sleep(1)
            print("ケン、", end='', flush=True)
            sleep(1)
            print("ポン", flush=True)
            sleep(0.5)
            print(self.hands[user_hond])
            print(self.hands[bot_hand])
            print("あなたは{}です。".format(self.decision[judge]))
        print("じゃんけんゲームを終わります。")


# メイン処理
obj = RockScissorsPaper()
obj.do()
