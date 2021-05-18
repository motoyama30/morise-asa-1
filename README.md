# ひたすら楽して音響信号解析 勉強会

小野研新入生向けの「ひたすら楽して音響信号解析」の輪読

- [出版社ホームページ](https://www.coronasha.co.jp/np/isbn/9784339009392/)
- [著者 GitHub ページ](https://github.com/mmorise/beginning_asa)

## 進め方

- 30~45 分で毎週 1 人が 1 章または 1 章の一部を講義する
- 残りの時間で本のコードを Python で実装する
- 1 人 1 問ずつ実装したコードを説明してもらう

**現在検討中です．やりながら今後変わる可能性があります．**

## 使い方

1. このレポジトリを clone する
   ```
   $ git clone https://github.com/onolab-tmu/morise-asa.git
   ```
2. コードを書いたら remote repository に push してください．
   ファイル名は `chapter<章番号>/<問題番号>.py` とし，章番号・問題番号は 1 始まりの 2 桁に揃えてください．
   例：1 章の 1 個目 → `chapter01/01.py`
   コミットメッセージは「○ 章を追加」などわかりやすい文章にしてください．
   ```
   $ git pull
   $ git add ./<user_name>/chpaterXX/YYY.py
   $ git commit -m 'your message'
   $ git push origin main
   ```

## 注意事項

- わからないところは **積極的** に RA か研究室の人に聞いてください．
- **他の人のディレクトリを変更しないでください．**
  - 他の人のコードを閲覧したい場合は、Web サイト上から閲覧してください．
- フォルダ名，ファイル名を間違えると進捗グラフに反映されません．

## 進捗状況

![progress](progress.png)

## 謝辞

[小町研究室](https://github.com/tmu-nlp)のいくつかのリポジトリを参考にしました．
