# import library 
import cv2 #opencv
import urllib.request
import numpy as np
from selenium import webdriver #webdriver
import time 

# webdriver object menggunakan firefox
profile = webdriver.FirefoxProfile()                                    
profile.set_preference("dom.forms.number", False)                       
driver = webdriver.Firefox(profile)
driver.get("http://192.168.4.1")

# webdriver element
turnleft = driver.find_element_by_id("turnleft")
turnright = driver.find_element_by_id("turnright")
forward = driver.find_element_by_id("forward")
backward = driver.find_element_by_id("backward")
turnLedOn = driver.find_element_by_id("flash")
turnLedOff = driver.find_element_by_id("flashoff")
streamCamera = driver.find_element_by_id("toggle-stream")
motorSpeed = driver.find_element_by_id("speed")

# streaming url
url = "http://192.168.4.1/capture"

# make opencv windows
cv2.namedWindow('drive', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('thresh', cv2.WINDOW_AUTOSIZE)

# center x and y array
CX = [50]
CY = [50]

# turn on LED
# turnLedOn.click()


# processing streaming and control
while True:
    # capture streaming
    imgResponse = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # rotate 90 degree
    img = img[100:250, :]


    # IMAGE PROCESSING
    # cropping image
    # belum diisi
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    # Color thresholding
    ret, thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)

    # DETECTION LINE
    # Find the contours of the frame
    contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        # find center of contour
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            CX.append(cx)
            CY.append(cy)
        else:
            cx = CX[-1]
            cy = CY[-1]

        # draw contour
        cv2.line(img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.drawContours(img, contours, -1, (0,255,0), 1)

        # CONTROLING ROBOT  
        if cx >= 120:
            # print ("Turn Left!")
            # time.sleep(0.25)
            motorSpeed.send_keys('100')
            turnleft.click()
        elif cx < 120 and cx > 50:
            # print ("On Track!")
            # time.sleep(0.25)
            motorSpeed.send_keys('125')
            forward.click()
        elif cx <= 50:
            # print ("Turn Right")
            # time.sleep(0.25)
            motorSpeed.send_keys('100')
            turnright.click()
        else:
            print("Oopps!")
            #backward.click()
        time.sleep(0.10)
        motorSpeed.clear()

    cv2.imshow('drive', img)
    cv2.imshow('thresh', thresh)
    key = cv2.waitKey(5)
    if key==ord('q'): # press q to quit
        break

cv2.destroyAllWindows