import cv2
#from PIL import Image
import numpy as np
from numpy import float32
import json
import codecs #for json format
from collections import OrderedDict
#from matplotlib import pyplot as plt
import operator

# for use 
#colorCube.colorHistCube( mean(h) , mean(s), mean(v)))

file_data = OrderedDict()
#file_data['det'] = []
#cap.set(cv2.CAP_PROP_FPS, int(5)) #frame control

global k
global q
i = 0
a = 0
s = 0
global list_h
global list_s
global list_v

with open('./colorHistResult/newsongdoCCTV/my1_hist_out.json') as json_file1:
    json_data1 = json.load(json_file1)
with open('./colorHistResult/newsongdoCCTV/ys3_2_hist_out.json') as json_file2:
    json_data2 = json.load(json_file2)
while(True):
    global k
    if len(json_data1['det'])> len(json_data2['det']):
        k = len(json_data2['det'])
    else:
        k = len(json_data1['det'])

    cmph = cv2.compareHist(cv2.UMat(np.array(json_data1['det'][i]['hist_h'], dtype=float32)), cv2.UMat(np.array(json_data2['det'][i]['hist_h'],dtype=float32)),cv2.HISTCMP_CORREL)
    cmps = cv2.compareHist(cv2.UMat(np.array(json_data1['det'][i]['hist_s'], dtype=float32)), cv2.UMat(np.array(json_data2['det'][i]['hist_s'],dtype=float32)),cv2.HISTCMP_CORREL)
    
    if( ( abs(cmph)>=0.15 or ( abs(cmph)>=0.10) and (abs(cmps))>=0.3 ) ): #0.5, 0.3, 0.2
        s = s + 1

    file_data[i+1]={'cmph':abs(cmph), 'cmps':abs(cmps)}
    # except: 
        # print('excepted')
    
    i = i + 1
    global q
    q = s
    if i == k:
        print('q:', float(q))
        print('k:', float(k)) 
        z = float(q) / float(k) 
        print('round z:', z )
        file_data['final']={'OverThreshold':s, 'Ratio': int(z * 100), 'Frame': k}
        break

    cv2.waitKey(50)


with open('./FinalCompareResult/1_my1_3_ys2.json','w' ) as make_file:
    json.dump(file_data,make_file,ensure_ascii=False, indent=4)
