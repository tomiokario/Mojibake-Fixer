# Mojibake-Fixer
UTF-8で保存された日本語テキストが別のエンコーディングとして解釈されることで発生する文字化けを修正する

## 概要

想定ケース：
- 誤ったエンコーディングで解釈された UTF-8 テキスト
- ダブルエンコーディング  

特徴：
- Pythonライブラリの`ftfy`[1]を活用してよくある文字化けパターンを自動修正
- 実行時に入力ファイルと出力ファイルを引数で指定する形式のPythonスクリプト
- UTF-8以外を想定する場合には、スクリプトの調整が必要

[1] Robyn Speer. (2019). ftfy (Version 5.5). Zenodo. http://doi.org/10.5281/zenodo.2591652

## 使い方

事前準備
- Python3の導入
- ftfyの導入

```bash
pip install ftfy
```

スクリプトの実行

```bash
python fix_encoding.py input.txt output.txt
```

- `input.txt` : 修正前の文字化けが発生しているテキストファイル
- `output.txt` : 修正後のテキストを出力するファイル
