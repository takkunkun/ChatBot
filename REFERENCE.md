<!-- 更新日：2023/01/07 -->
# 参考資料 <!-- omit in toc -->

PythonとGitHubを使う時に参考にしたサイトなどを載せる。

- [Python](#python)
  - [Pythonで対話式CLIツールを作る](#pythonで対話式cliツールを作る)
  - [他のファイルからインポートされたとき実行しない](#他のファイルからインポートされたとき実行しない)
  - [クラスのプロパティ（getter/setter）の書き方](#クラスのプロパティgettersetterの書き方)
  - [Pythonでifの複数条件（and・or）が不要になる【all・any】](#pythonでifの複数条件andorが不要になるallany)
- [GitHub](#github)
  - [Gitで特定のファイルだけをマージする](#gitで特定のファイルだけをマージする)
  - [バッチ作成](#バッチ作成)

# Python

Python使う時に参考にしたサイト

- [Pythonで対話式CLIツールを作る](#pythonで対話式cliツールを作る)
- [他のファイルからインポートされたとき実行しない](#他のファイルからインポートされたとき実行しない)
- [クラスのプロパティ（getter/setter）の書き方](#クラスのプロパティgettersetterの書き方)
- [Pythonでifの複数条件（and・or）が不要になる【all・any】](#pythonでifの複数条件andorが不要になるallany)

## Pythonで対話式CLIツールを作る

2022/12/17追加
  <https://qiita.com/skokado/items/50861b95b236068fd7b9>

  ```python
  import questionary
  ```

## 他のファイルからインポートされたとき実行しない

2022/12/17追加
  <https://blog.pyq.jp/entry/Python_kaiketsu_180207>

  ```python
  if __name__ == "__main__":
    pass
  ```

## クラスのプロパティ（getter/setter）の書き方

2023/01/06追加
  <https://naruport.com/blog/2019/8/27/python-tutorial-class-property-getter-setter/>

```python
class Cat:
    def __init__(self):
        self.__name = 'ミケ'

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name is None:
            raise TypeError('invalid name')
        self.__name = name
```

## Pythonでifの複数条件（and・or）が不要になる【all・any】

2022/01/07追加
<https://self-development.info/pythonでifの複数条件（and・or）が不要になる【all・any】/>
> **Note**
>
> - 「and」は「**all**」でOK
> - 「or」は「**any**」でOK
>
```python
if all([a, b, c, d, e]):
    print("全部True")
else:
  print("どれか一つはFalse")
```

```python
if any([a, b, c, d, e]):
    print("どれか一つはTrue")
else:
    print("全部False")
```
## pyinstallerで作ったwindowsアプリでバージョンを表示させたいversion_resource_fileの作りかた
<https://nobwak.github.io/posts/2014-05-09-pyinstallerで作ったwindowsアプリでバージョンを表示させたいversion_resource_fileの作りかた/>

# GitHub

GitHub使う時に参考にしたサイト

- [Gitで特定のファイルだけをマージする](#gitで特定のファイルだけをマージする)
- [バッチ作成](#バッチ作成)

## Gitで特定のファイルだけをマージする

2022/12/17追加
<https://scrapbox.io/kijisaba-memo/Gitで特定のファイルだけをマージする>

  ```bash
  git checkout <ブランチ名> -- <ファイル名>
  ```

## バッチ作成

2023/01/05追加
<https://kic-yuuki.hatenablog.com/entry/2019/06/29/173256>
<https://shields.io/>
例）![Python3.10](https://img.shields.io/badge/python-v3.10-blue "Python3.10")
