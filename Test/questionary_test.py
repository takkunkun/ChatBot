import questionary
from questionary import Validator, ValidationError, prompt
from typing import Any


# class NameValidator(Validator):
#     def validate(self, document):
#         if len(document.text) == 0:
#             raise ValidationError(
#                 message="Please enter a value",
#                 cursor_position=len(document.text),
#             )

# questionary.text("What's your name?", validate=NameValidator).ask()

min = 0
max = 999
UserName = "you"


class NumValidator(Validator):
    def validate(self, document: Any) -> None:
        text = document.text
        if len(text) == 0:
            raise ValidationError(
                message="値を入力してください。",
                cursor_position=len(text),
            )
        try:
            text = int(text)
        except ValueError:
            raise ValidationError(
                message="数値を入力してください。\n数値以外が入力されています。",
            )
        if (text < min) or (max < text):
            raise ValidationError(
                message=f"{min}以上{max}以下で入力してください。",
            )


while True:
    ans = questionary.text(
        "数値：",
        qmark=(f"{UserName} >"),
        validate=NumValidator
    ).ask(kbi_msg="キャンセルされました。")
    if ans is None:
        # questionaryで「KeyboardInterrupt」の場合、Noneが返ってくる
        break

if ans is not None:
    ans = int(ans)

print(ans)
