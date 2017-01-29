# Docker って何よ！
コンテナ型の仮想環境管理ツール群の総称

## コンテナって何よ！
外部環境から独立した環境

## VM と違うの
違う

- カーネルはホストと共有してるので軽い
- 起動・停止のオーバーヘッドを削減してる

## で Docker なにがいいの
- 気軽にサービスを試せる
- 複数の環境を走らせられる
- かわいい


# やるぞ

https://github.com/suzuki-shunsuke/docker-learning

## Dockerツール

- Docker Engine  
	Docker コマンドツール群
- Docker Hub  
	Docker Image のホスティングクラウド
- Docker Composer  
	Docker Image 群の bundling
- Docker Machine  
	Docker Engine のインストーラ
- Kubernetes
- etc

PaaSにも乗ってるのですごくいい。


# Docker Image 作るぞ

Dockerfile作ってdockerbuildするよ。
Ansibleとか使うよ


# Docker Image のレイヤモデル

レイヤ毎の適用 -> 差分だけ取ってこれる、レイヤ単位で処理できる。
コマンドごとにレイヤを重ねていくイメージ
diffがそのままレイヤモデルになってる


# Automated Build
GitHubでDockerfileをホスティングし、
GitHubリポジトリのpushにhookして、環境を自動ビルド
