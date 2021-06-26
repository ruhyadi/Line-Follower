import cv2
import numpy as np

def centers(moments, x):
    if moments["m00"] == 0:
        return 0
    else:
        if x == 0:
            return int(moments["m10"]/moments["m00"])
        else:
            return int(moments["m01"]/moments["m00"])

def SlicePart(image, slices, i):
	height, width  = image.shape[:2]
	sl = int(height/slices);
	part = sl*(i-1)
	crop_img = image[part:part+sl, 0:width]

	return crop_img

def ImProcess(frame):
    pointsList = [[0, 0]]
    imgList = []
    direction = 0
    # frame = cv2.blur(frame,(10,10)) #Blur the image to smooth the contour
    for i in range(9):
        imgList.append(SlicePart(frame, 8, i)) #Slice the frame in 4 parts and add them to the array
    for l in range(1,9): # For every slice in each frame
        im = imgList[l]
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Convert to Gray Scale
        thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,99,10)
        # ret, thresh = cv2.threshold(imgray,100,255,cv2.THRESH_BINARY_INV) #Get Threshold
        contours, hierarchy = cv2.findContours(thresh, 1,cv2.CHAIN_APPROX_SIMPLE) #Get contour of each slice

        height, width  = im.shape[:2]
        center = None

        middleX = int(width/2) #Get X coordenate of the middle point
        middleY = int(height/2) #Get Y coordenate of the middle point

        if contours: # If has found a contour
            c = max(contours, key=cv2.contourArea) #Get the largest contour

            #----------- Contour Center---------------
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            cX = centers(M,0)
            cY = centers(M,1)
            #/////////// Contour Center///////////////

            direction += (middleX-cX) #Calculate the direction to turn

            pointsList.append([cX, cY+(int(height)*(l-1))]) #Add the center of point to the array

            cv2.drawContours(im,contours,-1,(0,255,0),1) #Draw Contour GREEN
            cv2.circle(im, (cX, middleY), 3, (255,255,255), -1) #Draw dX circle WHITE
            cv2.circle(im, (middleX, middleY), 3, (0,0,255), -1) #Draw middle circle RED

            #Calculate dX = middleX-cX

            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(im,str(middleX-cX),(cX+20, cY), font, 1,(175,175,175),2,cv2.LINE_AA) # Text that indicates dX
        else:
            cX_ = pointsList[-1][0]
            cY_ = pointsList[-1][1]
            pointsList.append([cX_, cY_+(int(height)*(l-1))]) #Add the center of point to the array

    vis = np.concatenate((
        np.concatenate((imgList[1], imgList[2]), axis=0), 
        np.concatenate((imgList[3], imgList[4]), axis=0),
        np.concatenate((imgList[5], imgList[6]), axis=0),
        np.concatenate((imgList[7], imgList[8]), axis=0),
        ), axis=0) #Repack all the slices to a complete image

    cv2.polylines(vis, np.int32([pointsList]), 1, (255,0,0)) #Draw line over the points of each slice

    # #Flush the data
    del imgList[:] 
    # del pointsList[:]
    direction = direction/8
    turn = int(pointsList[4][0])

    return vis, direction, pointsList, turn