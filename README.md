[English Ver.](#english)
[Japanese Ver.](#japanese)

<a name="english"/> 

# EC_crawler (English ver.)

<a name="japanese"/>

# ECサイトクローラー（日本語版）

## 開発背景・目的

- 価格.comを代表とする買い物支援サイトは在庫希少品や人気商品の価格変動に対してリアルタイム性に欠けている
- Nintendo Switchをいち早く定価で買うために

## インフラ構成図

![スクリーンショット 2019-08-12 10 42 48](https://user-images.githubusercontent.com/36617009/62842624-478a6000-bcee-11e9-9304-9a6e4bb368cd.png)

## 特徴・オリジナル性

- 時系列分析による自動スケジューリング

## 機能

- 能動的なクローリング方式で瞬時（10分以内）の在庫を把握
- 予め設定した目標価格を発見次第、シームレスにユーザー端末に通知
- 時系列分析でスケジューラトリガーを最適化し、ホスティングコストを圧縮

## 実装環境

- Scrapyフレームワークでのローカル実装
- AWSでフルクラウドアーキテクチャ、さらにサーバーレスでリアルタイムコンピューティングのAWS Lambdaを採用したFaaS（Function as a Service）方式

