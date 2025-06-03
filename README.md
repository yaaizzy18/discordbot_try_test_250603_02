# Discord Bot Test

テスト用のDiscordボットのプロジェクトです。

## 機能
- `!hello`: こんにちはメッセージを返す
- `!ping`: ボットの応答時間を表示

## セットアップ
1. Discord Developer Portalで新しいアプリケーションを作成し、Botを追加
2. `.env`ファイルの`DISCORD_TOKEN`にBotトークンを設定
3. 以下のコマンドで必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

## 起動
```bash
python bot.py
```
