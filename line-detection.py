import cv2
import urllib.request
import numpy as np

url = "http://192.168.4.1/capture"
cv2.namedWindow('stream', cv2.WINDOW_AUTOSIZE)



while True:
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow('stream', img)
    key = cv2.waitKey(5)
    if key==ord('q'):
        break

cv2.imwrite('image_scan/image-3.jpg', img)
cv2.destroyAllWindows
