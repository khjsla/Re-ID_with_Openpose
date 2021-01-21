#CAMERA1
import cv2
#from PIL import Image
import numpy as np
import json
import time
import codecs #for json format
from collections import OrderedDict
from matplotlib import pyplot as plt
import operator

# for use 
#colorCube.colorHistCube( mean(h) , mean(s), mean(v)))

file_data = OrderedDict()
file_data['det'] = []

cap = cv2.VideoCapture('./songdoCCTV/mov/js/js1_1.mov')
#cap.set(cv2.CAP_PROP_FPS, int(5)) #frame control


print('width :%d, height : %d' % (cap.get(3), cap.get(4)))
width = cap.get(3)
height = cap.get(4)

global k
i = 0
a = 0

global list_h
global list_s
global list_v

with open('./colorROIsetting/songdoCCTV/js1_1.json') as json_file:
    json_data = json.load(json_file)
while(True):
    try:
        ret, frame = cap.read()    # Read output and frame
        imCrop = cv2.resize(frame, (1920, 1080)) #1280, 720 #1920, 1080
        h, w, l = imCrop.shape

        # key is json_number number import
        json_roi = json_data['det'][i]['people']
        if not json_roi:
            imCrop2 = imCrop
            print("no person")
            pass
        else: 
            frame_id = json_data['det'][i]["frame_id"] #cam1 = ori # cam2 = +20
            roi_1 = json_data['det'][i]['people']["1"]
            roi_11 = json_data['det'][i]['people']["11"]
            roi_8 = json_data['det'][i]['people']["8"]

            if (int(roi_11[0]) > 0) and (int(roi_11[1]) > 0) and (int(roi_8[0]) > 0) and (int(roi_8[1]) > 0) and (int(roi_1[0]) > 0) and (int(roi_1[1]) > 0):
                #print ("neck y:", int(roi_1[0]),"neck x:",int(roi_1[1]) ,"Lhip y:",int(roi_11[0]),"Lhip x:",int(roi_11[1]),"Rhip y:",int(roi_8[0]),"Rhip x:",int(roi_8[1])) #float -> int
                #print(roi_1, roi_11, roi_8)  # cause number, str()use
                # 720 : 1280
                #imCrop2 = imCrop[int(roi_1[1]):int(roi_11[1])-1, int(roi_8[0]):int(roi_11[0])-1] #dy version
                global k
                if int(roi_11[1]) > int(roi_8[1]) : k = int(roi_8[1])
                else : k = int(roi_11[1])
                #print k #ok

                xl = int( roi_8[0] - 0.05*( roi_11[0] - roi_8[0] ) ) 
                yh = int( roi_1[1] - 0.2*( roi_1[1] - k )) 
                xr = int( roi_11[0] + 0.05*( roi_11[0] - roi_8[0] ) ) 
                yl = int( k )

                if ( xr - xl > 0) and ( yl - yh > 0): #face : >
                    imCrop2 = imCrop[ yh : yl , xl : xr ] # face: xl:xr
                    print('what is pixel len of ROI:', len(imCrop2)) # divide this to calcHist
                    
                    if(len(imCrop2)<140):
                        pass
                    else:
                        hsv_frame = cv2.cvtColor(imCrop2, cv2.COLOR_BGR2HSV) #convert to hsv
                        h,s,v = cv2.split(hsv_frame) #distibute imCrop ROI area to h,s,v part 
                        h = h - 10
                        # # #h = ((h.astype('int16')-100)%180).astype('uint8')
                        hsv_frame = cv2.merge([h,s,v])

                        hist_h = cv2.calcHist([hsv_frame],[0],None,[180],[0,180]) / len(imCrop2)
                        cv2.normalize(hist_h,hist_h,0,1,cv2.NORM_MINMAX)
                        hist_s = cv2.calcHist([hsv_frame],[1],None,[256],[0,256]) / len(imCrop2)
                        cv2.normalize(hist_s,hist_s,0,1,cv2.NORM_MINMAX)
                        # Normalize histograms based on number of pixels per frame.
                        plt.plot(hist_h)
                        plt.xlim([0,180])
                        plt.show()

                        file_data['det'].append({'FrameNumber' : i+1})
                        file_data['det'][a] = {'hist_h': hist_h.tolist(), 'hist_s': hist_s.tolist() }
                        #JSON encoding
                        a = a+1
                elif ( xr - xl < 0) and ( yl - yh > 0): #face : >
                    imCrop2 = imCrop[ yh : yl , xr : xl ] # face: xl:xr
                    print('what is pixel len of ROI:', len(imCrop2)) # divide this to calcHist
                        
                    if(len(imCrop2)<140):
                        pass
                    else:
                        hsv_frame = cv2.cvtColor(imCrop2, cv2.COLOR_BGR2HSV) #convert to hsv
                        h,s,v = cv2.split(hsv_frame) #distibute imCrop ROI area to h,s,v part 
                        h = h - 10
                        # # #h = ((h.astype('int16')-100)%180).astype('uint8')
                        hsv_frame = cv2.merge([h,s,v])

                        hist_h = cv2.calcHist([hsv_frame],[0],None,[180],[0,180]) / len(imCrop2)
                        cv2.normalize(hist_h,hist_h,0,1,cv2.NORM_MINMAX)
                        hist_s = cv2.calcHist([hsv_frame],[1],None,[256],[0,256]) / len(imCrop2)
                        cv2.normalize(hist_s,hist_s,0,1,cv2.NORM_MINMAX)
                        
                        plt.plot(hist_h)
                        plt.xlim([0,180])
                        plt.show()

                        # Normalize histograms based on number of pixels per frame.
                        
                        file_data['det'].append({'FrameNumber' : i+1})
                        file_data['det'][a] = {'hist_h': hist_h.tolist(), 'hist_s': hist_s.tolist() }
                        #JSON encoding
                        a = a+1
                else:
                    #print("xr-xl:",xr-xl,"yh-yl:",yh-yl)
                    #print("skip err?")
                    imCrop2 = imCrop
                    pass
            else:
                #print("no upper body")
                # under neck position, print only neck
                pass        
    except: 
        imCrop2 = imCrop
        #print('excepted')
    
    i = i + 1
    if i == len(json_data['det']):
        break

# noise remove
    #imCrop2 = cv2.bilateralFilter(imCrop2, 9, 75, 75)
#   imCrop2 = cv2.GaussianBlur(imCrop2, (5, 5), 0)

# inserting text on video 

    #cv2.imshow('ROI',imCrop2)

#   # cv2.imshow("Image window", cv_image)
    cv2.waitKey(5)

cap.release()
# cv2.destroyAllWindows()

#print(json.dumps(file_data, ensure_ascii = False))

with open('./colorHistResult/newsongdoCCTV/js1_1_hist_out.json','w' ) as make_file:
    json.dump(file_data,make_file,ensure_ascii=False, indent=4)
