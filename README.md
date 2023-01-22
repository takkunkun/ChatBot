# ChatBot  <!-- omit in toc -->

![python3.10](https://img.shields.io/badge/python-v3.10-blue "Python3.10")

## 目次 <!-- omit in toc -->

- [機能一覧](#機能一覧)
- [必要なライブラリ](#必要なライブラリ)
- [ライブラリのインストール方法](#ライブラリのインストール方法)
- [使い方](#使い方)
- [備考](#備考)
- [exeの作成方法](#exeの作成方法)

## 機能一覧

  1. 自己紹介
  2. 曜日当てゲーム
  3. じゃんけんゲーム
  4. 郵便番号から住所検索
  5. 数当てゲーム

## 必要なライブラリ

"ChatBot"を動かすのに必要なライブラリ

- [colorama](https://github.com/tartley/colorama)
（文字色を変えるライブラリ）
- [questionary](https://github.com/tmbo/questionary)
（きれいなコマンドラインインターフェイスのライブラリ）
- [requests](https://github.com/psf/requests)
（HTTPライブラリ）

## ライブラリのインストール方法

[必要なライブラリ](#必要なライブラリ)で列挙したライブラリのインストール方法

### pipの場合 <!-- omit in toc -->

```bash
pip install colorama
```

```bash
pip install questionary
```

```bash
pip install requests
```

### Anacondaの場合 <!-- omit in toc -->

```bash
conda install colorama
```

```bash
conda install -c conda-forge questionary
```

```bash
conda install requests
```

## 使い方

"ChatBot"の基本的な使い方を説明する

```bash
python chatbot.py
```

## 備考

`1.自己紹介`を実行した場合、「`username.txt`」にユーザー名が保存される。

## exeの作成方法

exeの作成には、「`pyinstaller`」を使用した。

### pipの場合 <!-- omit in toc -->

```bash
pip install pyinstaller
```

### Anacondaの場合 <!-- omit in toc -->

```bash
conda install pyinstaller
```

### 作成 <!-- omit in toc -->

```bash
pyinstaller --onefile chatbot.py
```
