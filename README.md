# tello-drone-image-caption-and-object-detection

<img width="1416" alt="github_pic" src="https://user-images.githubusercontent.com/87643752/128824725-aaf3fabb-2f2b-47a5-8982-a23e592e6346.png">


## **使い方** 

1. このリポジトリの資源をgit cloneしたノートPCを、TelloにWifi接速する。
2. **examplesディレクトリ**に移動して、Python3系で、**tello_camera_image_captioned_description_window.py**を実行する。

> % python3 tello_camera_image_captioned_description_window.py


### 1. Telloドローンのキーボード操作

TelloとWifi回線でつながっているノートPCのキーボードから、Telloを操作します。

* i : 離陸
* w: 前進
* s : 後進
* a : 左移動
* d : 右移動
* e : 時計回り30度回転
* q : 反時計回り30度回転
* r :  上昇
* f :  降下
* g : 着地
* p : フレーム画像のファイル保存（※）

※ 画像ファイルは、カレントディレクトリ（exampleディレクトリ直下）に出力されます。

※ ファイル名は。**frame_img_shot_XXXX年XX月XX日XX/XX/XX.jpg**です。最後はhour, minutes, ミリ秒です。

### 2. Telloカメラ画像のウィドウ表示（左右２画面）

離陸前から、ノートPCにWindowが１つ立ち上がり、画面の左側にTelloから受信したカメラ画像（原画像）が表示され、右側には、画像の内容を説明した英文が表示されます。

右画面に出力される説明文は、次のリポジトリの資材を利用します。

- https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning

画面の左側に表示されるTelloカメラ画像の受信は、**DJITelloPyライブラリ**を使います。

- https://github.com/damiafuentes/DJITelloPy

## __事前準備__

### このリポジトリの資源の取得

このリポジトリ内の資源を、ここにある通りのディレクトリ構成でダウンロードしてください。（git clone又は手動zipダウンロード）

### 資源の追加取得

画像のキャプション文を生成する処理は、次のリポジトリの資源を借用しています。
次のリポジトリの指示通り、DropBoxから学習済みのモデルとボキャブラリファイルをダウンロードしてください。
ダウンロード後、次に述べるディレクトリに格納します。

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

