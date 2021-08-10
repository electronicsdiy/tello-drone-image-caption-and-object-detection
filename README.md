# tello-drone-image-caption-and-object-detection

#__使い方__ 

1. このリポジトリの資源をgit cloneしたノートPCを、TelloにWifi接速する。
2. __*examples*ディレクトリ__に移動して、Python3系で、__*tello_camera_image_captioned_description_window.py*__を実行する。

> % python3 tello_camera_image_captioned_description_window.py


##1. Telloドローンのキーボード操作

__DJITelloPyライブラリ__を利用して、TelloとWifi接続したノートPCからキーボード操作でTelloを操作します。
__DJITelloPyライブラリ__を使うことで、Tello内蔵の単眼カメラが捉えた映像データを、ノートPC側でリアルタイムに受信します。

#__事前準備__

##2. フレーム画像の説明（キャプション）文生成

Telloからコントローラー（PC）に送られてくる各瞬間のフレーム画像（numpy行列オブジェクト）から、画像の説明文を得るデータ処理は、次のリポジトリの実装コードを利用しています。

- https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning

このリポジトリの解説に従って、学習済みのモデルファイルをダウンロードして、所定のディレクトリに格納する必要があります。

###資源のダウンロード

1. 以下から学習済みのモデルファイルをダウンロードし、ファイル名を変更後、example/modelsの直下に格納してください。

- decoder-5-3000.pkl
- encoder-5-3000.pkl

https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0

（ファイル名の変更方法）

encoder-5-3000.pkl → encoder-2-1000.ckpt
decoder-5-3000.pkl → decoder-2-1000.ckpt

2. 以下から学習済みのボキャブラリファイルをダウンロードし、example/dataの直下に格納してください。

https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0

