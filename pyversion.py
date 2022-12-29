# https://note.nkmk.me/python-sys-platform-version-info/
# https://atmarkit.itmedia.co.jp/ait/articles/2111/30/news020.html
import sys
major = sys.version_info.major
minor = sys.version_info.minor
micro = sys.version_info.micro
print(f"Python {major}.{minor}.{micro}")

if ((major >= 4) or (major >= 3 and minor >= 10)):
    print("3.10以上です。")
else:
    raise RuntimeError("3.10未満です。")
