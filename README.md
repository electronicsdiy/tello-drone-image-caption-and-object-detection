# tello-drone-image-caption-and-object-detection

## **使い方** 

1. このリポジトリの資源をgit cloneしたノートPCを、TelloにWifi接速する。
2. **examplesディレクトリ**に移動して、Python3系で、**tello_camera_image_captioned_description_window.py**を実行する。

> % python3 tello_camera_image_captioned_description_window.py


####1. Telloドローンのキーボード操作

TelloとWifi回線でつながっているノートPCのキーボードから、Telloを操作します。
また、ノートPCにWindowが１つ立ち上がり、左右2画面に分割されたWindowが立ち上がります。

Telloのキーボード操作と画像受信の処理は、**DJITelloPyライブラリ**を使います。

- https://github.com/damiafuentes/DJITelloPy

ノートPCにWindowが１つ立ち上がる画面は、左右2画面に分かれています。

・ **左画面**： 各瞬間のフレーム画像の内容を説明した英文が、背景黒地の画面に白文字で表示。
・ **右画面**： Telloから受信したフレーム画像の上に、検出された物体を四角（矩形）の枠で囲み、オブジェクト名を英単語で書かれます。また、Telloの現在高度が表示される。

Telloから受け取った各瞬間のフレーム画像の内容を説明する文を、PC側で出力する処理は、次のリポジトリの資材を利用します。

- https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning

## __事前準備__

####資源のダウンロード

画像のキャプション文を生成する処理を行うために、借用した次のリポジトリの指示通り、学習済みのモデルとボキャブラリファイルをdropboxからダウンロードして、
指定されたディレクトリに格納します。

- https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning

1. 以下から学習済みのモデルファイルをダウンロードし、ファイル名を変更後、example/modelsの直下に格納してください。

- decoder-5-3000.pkl
- encoder-5-3000.pkl

https://www.dropbox.com/s/ne0ixz5d58ccbbz/pretrained_model.zip?dl=0

ファイル名の変更

encoder-5-3000.pkl → encoder-2-1000.ckpt
decoder-5-3000.pkl → decoder-2-1000.ckpt

2. 以下から学習済みのボキャブラリファイルをダウンロードし、example/dataの直下に格納してください。

https://www.dropbox.com/s/26adb7y9m98uisa/vocap.zip?dl=0

