from common import *

TIMEOUT_SEC = 0.1

@timeout(TIMEOUT_SEC)
def input_with_timeout(msg=None):
   return input(msg)


tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

#tello.takeoff()

while True:
    img = frame_read.frame
    #cv2.imshow("drone", img)
    #cv2.imshow('Canny', cv2.Canny(img, 100, 200))
    #bitwised_img = cv2.bitwise_not(img)
    #cv2.imshow('Bitwised', bitwised_img)
    
    image = img.copy()

    # 物体検出矩形表示と人物検出人数の文字列埋込み表示の画像を取得
    label_name  = "person"
    bbox, label, conf = cvl.detect_common_objects(image)
    objection_detected_image = draw_bbox(image, bbox, label, conf)
    #plt.imshow(objection_detected_image)
    #plt.show()
    #dt_now = datetime.datetime.now()
    message = "Num of detected {0}(s) is {1}".format(label_name, str(label.count(label_name)))
    input_text_0 = message
    cv2.putText(objection_detected_image, str(input_text_0), (0, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
    
    #https://djitellopy.readthedocs.io/en/latest/tello/#djitellopy.tello.Tello.query_battery
    time_of_flight_distance_senser_val = tello.get_distance_tof()
    input_text_1 = "ToF Distane {0} cm".format(time_of_flight_distance_senser_val)
    
    height = tello.get_height()
    input_text_2 = "Height {0} cm".format(height)
 
    height = objection_detected_image.shape[0]
    width = objection_detected_image.shape[1]
    print("height {0}".format(height))
    print("width {0}".format(width))
    # Terminal標準出力
    print(input_text_0)
    print(input_text_1)
    print(input_text_2)
    
    # カメラ画像にTelloの現在高度（ToFセンサ計測距離(cm)、高さ（cm)）を埋込む
    cv2.putText(objection_detected_image, str(input_text_1), (0, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(objection_detected_image, str(input_text_2), (0, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
    #cv2.imshow("Video_2", objection_detected_image)
    
    caption_text_list = create_caption_text_str_list(img)
    
    print("\n現在のフレーム画像の状況説明文")
    #listの各要素（キャプション文を40文字毎に切り出した各行）を改行しながら順に表示
    pprint(caption_text_list)
    print("====================================")
    
    #背景黒地の画面に、キャプション文を埋込む
    #white_bachground_img = np.zeros((height, width,3), np.uint8)

    # https://qiita.com/daxanya1/items/85f5e17ecc1203f756ad
    # https://qiita.com/tifa2chan/items/78d4af969cfa837fa988
    # 背景黒の画面。zerosの引数がheightが先になるので注意
    black_bachground_img = np.zeros((height, width, 3),np.uint8)
    # 背景白にする場合。
    #white_bachground_img = np.full((height, width, 3), 255, dtype=img.dtype)

    for i, caption_sentence in enumerate(caption_text_list):
        cv2.putText(black_bachground_img, str(caption_sentence), (50, 80+i*70), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    #cv2.imshow("Video_1", black_bachground_img)
    
    # 2つの画像を１つのウィンドウに組込む
    merged_image_group = cv2.hconcat((black_bachground_img, objection_detected_image))
    
    height = merged_image_group.shape[0]
    width = merged_image_group.shape[1]
    resized_output_img = cv2.resize(merged_image_group, (int(1.7*width), int(1.7*height)))
    
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.imshow("Video", resized_output_img)
    
    #次の行（key = cv2.・・・）を削除すると、画像が受信できなくなる。
    key = cv2.waitKey(1) & 0xff
    
    try:
        msg = input_with_timeout('\n{}秒以内に操作コマンドを入力して下さい :'.format(TIMEOUT_SEC))
        print('\n操作コマンド：　{} を受信しました。\n'.format(msg))
        if msg == "i":
            tello.takeoff()
        elif msg == "w":
            tello.move_forward(30)
        elif msg == "s":
            tello.move_back(30)
        elif msg == "a":
            tello.move_left(30)
        elif msg == "d":
            tello.move_right(30)
        elif msg == "e":
            tello.rotate_clockwise(30)
        elif msg == "q":
            tello.rotate_counter_clockwise(30)
        elif msg == "r":
            tello.move_up(30)
        elif msg == "f":
            tello.move_down(30)
        elif msg == "g":
            tello.land()
        elif msg == "p":
            dt_now = datetime.datetime.now()
            timestamp_str = dt_now.strftime('%Y年%m月%d日%H:%M:%S')
            file_name = "frame_img_shot_{0}.jpg".format(timestamp_str)
            cv2.imwrite(file_name, resized_output_img)
            print("フレーム画像を保存しました。")
    except TimeoutError:
        print('\n操作コマンド入力時間切れ。次のフレーム画像を読み込みます。\n')

tello.land()
