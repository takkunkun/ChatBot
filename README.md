# ChatBot
![python3.10](https://img.shields.io/badge/python-v3.10-blue)

# 目次
- [ChatBot](#chatbot)
- [目次](#目次)
- [Functions](#functions)
- [Requirements](#requirements)
- [Installations](#installations)
  - [pipの場合](#pipの場合)
  - [Anacondaの場合](#anacondaの場合)
- [Usage](#usage)
  - [Note](#note)
- [How to make exe](#how-to-make-exe)
  - [pipの場合](#pipの場合-1)
  - [Anacondaの場合](#anacondaの場合-1)
  - [作成](#作成)


# Functions
  1. 自己紹介
  2. 曜日当てゲーム
  3. じゃんけんゲーム
  4. 郵便番号から住所検索

# Requirements
"ChatBot"を動かすのに必要なライブラリ
* [colorama](https://github.com/tartley/colorama)
（文字色を変えるライブラリ）
* [questionary](https://github.com/tmbo/questionary)
（きれいなコマンドラインインターフェイスのライブラリ）
* [requests](https://github.com/psf/requests)
（HTTPライブラリ）

# Installations
Requirementで列挙したライブラリなどのインストール方法
## pipの場合
```bash
pip install colorama
```
```bash
pip install questionary
```
```bash
pip install requests
```
## Anacondaの場合
```bash
conda install colorama
```
```bash
conda install -c conda-forge questionary
```
```bash
conda install requests
```

# Usage
"ChatBot"の基本的な使い方を説明する
```bash
python chatbot.py
```

## Note
自己紹介を実行した場合、「username.txt」にユーザー名が保存される。

# How to make exe
exeの作成には、「pyinstaller」を使用した。
## pipの場合
```bash
pip install pyinstaller
```
## Anacondaの場合
```bash
conda install pyinstaller
```
## 作成
```bash
pyinstaller --onefile chatbot.py
```