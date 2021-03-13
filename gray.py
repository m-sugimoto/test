import cv2


img = cv2.imread("/Users/sugimotomamoru/python/テスト画像/fanza2-2.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("/Users/sugimotomamoru/python/結果画像/fanza2-2mono.jpg", img)

