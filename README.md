# IaaS-team-1
## Rest API Server
/restAPI/api.pyがRest API Serverである．

1. Ubuntu にpythonとflaskを入れる
1. Dockerをインストールする
1. ホームフォルダにdockerフォルダをつくる
1. sudo ./api.pyを実行
 
## CLI
/restAPI/iaasがコマンドである．

1. Ubuntuにpythonとcurlをインストールする
1. ./iaas でコマンドを実行する(詳細は-hで参照可)

## Controller VM
Virtual Box にインポートして使用する．パスワードは "ensyuu2"． 

有線 LAN (クロスオーバー) で VM を起動している端末とスイッチのマネジメントポートとを接続しておく．その後，以下のコマンドを実行する．

```
cd one_switch
./if.sh
./bin/trema run ./lib/one_switch.rb
```

以下，各コマンドの説明

1. cd コマンドで one_switch ディレクトリに移動
1. if.sh を 実行する．NIC の設定が行われる．
1. コントローラのプログラムを起動する．

### 各種設定
one_switch ディレクトリ中の one_switch.conf にて必要な設定を記入．

1. SERVER_IP_ADDRESS にサーバーとして用いるホストの IP アドレスを記入．
1. ACCESS_LIMITATION_INTERVAL (T) と ACCESS_LIMITATION_COUNT (n) を記入して，アクセス制限の設定を行う．直近の T 秒間である IP アドレスからのアクセスが n 回あった場合，そのIPからのアクセスを遮断

## スイッチに接続するホストの設定
OS は Ubuntu を想定．物理ホスト，仮想ホストのいずれも可．git をインストールしておく．

以下のコマンドを実行して Iaas-team-1 の git をダウンロード

```
git clone https://github.com/handai-trema/Iaas-team-1.git
```

仮想ホストの場合はこの後パワーオフし，仮想化ソフトウェアの設定にてネットワーク接続の種類を「ブリッジアダプター」に変更する．

有線 LAN でホストとスイッチのポートを接続し，以下のコマンドを実行

```
cd Iaas-team-1
chmod 755 host.sh
./host.sh [接続に使用するインターフェース名] [接続するスイッチポートの番号]
```
