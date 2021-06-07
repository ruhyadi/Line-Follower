# import library 
import cv2 #opencv
import urllib.request
import numpy as np
from selenium import webdriver #webdriver

# webdriver object menggunakan firefox
driver = webdriver.Firefox()
driver.get("http://192.168.4.1")

# webdriver element
turnleft = driver.find_element_by_id("turnleft")
turnright = driver.find_element_by_id("turnright")
forward = driver.find_element_by_id("forward")
backward = driver.find_element_by_id("backward")
turnLedOn = driver.find_element_by_id("flash")
turnLedOff = driver.find_element_by_id("flashoff")
streamCamera = driver.find_element_by_id("toggle-stream")

# streaming url
url = "http://192.168.4.1/capture"

# make opencv windows
cv2.namedWindow('drive', cv2.WINDOW_AUTOSIZE)

# processing streaming and control
while True:
    # capture streaming
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # rotate 90 degree

    cv2.imshow('drive', img)
    key = cv2.waitKey(5)
    if key==ord('q'): # press q to quit
        break

cv2.destroyAllWindows
