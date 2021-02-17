import sys
import cv2

# カメラを開く
cap = cv2.VideoCapture(0)
# カメラが開けなかったとき
if not cap.isOpened():
    print('Can not open camera')
    sys.exit()
# 表示ウィンドウの作成
cv2.namedWindow('win_dst', cv2.WINDOW_NORMAL)
# ウィンドウサイズを変更
cv2.resizeWindow('win_dst', 800, 600)

rec = cv2.VideoWriter('data/traning3.mp4', cv2.VideoWriter_fourcc(*'H264'),
                      5)

# ループ開始
while True:
    # 1フレーム読み込み
    ret, src = cap.read()
    # カメラからフレームが読み込めなかったら中断
    if not ret:
        break

    dst = cv2.flip(src, 1)                # 左右反転
    #dst = cv2.stylization(src)            # イラスト風
    #gray, dst = cv2.pencilSketch(src)     # 鉛筆画風

    # 入力と出力を1フレーム表示
    cv2.imshow('win_src', src)
    cv2.imshow('win_dst', dst)
    key = cv2.waitKey(30)
    if cv2.waitKey(10) == 27:
        break

    if key == ord(' '):
        # 1フレーム書き込み
        rec.write(src)
        # 現在フレームを前フレームに複製
        prev = src.copy()
        count += 1
    elif key == 27:
        break

cv2.destroyAllWindows()
# カメラを閉じる
cap.release()