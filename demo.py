
import cv2
import numpy as np
from MtcnnDetector import FaceDetector



if __name__ == '__main__':   
 
    img = cv2.imread('1.jpg')
    detector = FaceDetector(minsize = 20, gpuid = 1, fastresize = False) 
    total_boxes,points,numbox = detector.detectface(img)
    
    for i in range(numbox):
        cv2.rectangle(img,(int(total_boxes[i][0]),int(total_boxes[i][1])),(int(total_boxes[i][2]),int(total_boxes[i][3])),(0,255,0),2)        
        for j in range(5):        
            cv2.circle(img,(int(points[j,i]),int(points[j+5,i])),2,(0,0,255),2)

    cv2.imwrite( '1_out.jpg',img )
    print 'Done.'