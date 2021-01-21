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

file_data1 = OrderedDict()
file_data2 = OrderedDict()
file_data3 = OrderedDict()
file_data4 = OrderedDict()
file_data5 = OrderedDict()

file_data6 = OrderedDict()
file_data7 = OrderedDict()
file_data8 = OrderedDict()
file_data9 = OrderedDict()
file_data10 = OrderedDict()

file_data11 = OrderedDict()
file_data12 = OrderedDict()
file_data13 = OrderedDict()
file_data14 = OrderedDict()
file_data15 = OrderedDict()

file_data16 = OrderedDict()
file_data17 = OrderedDict()
file_data18 = OrderedDict()
file_data19 = OrderedDict()
file_data20 = OrderedDict()

file_data21 = OrderedDict()
file_data22 = OrderedDict()
file_data23 = OrderedDict()
file_data24 = OrderedDict()
file_data25 = OrderedDict()

file_data26 = OrderedDict()
file_data27 = OrderedDict()
file_data28 = OrderedDict()

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

with open('./colorHistResult/newsongdoCCTV/hj1_hist_out.json') as json_file1:
    json_data1 = json.load(json_file1)
with open('./colorHistResult/newsongdoCCTV/hj2_1_hist_out.json') as json_file2:
    json_data2 = json.load(json_file2)
with open('./colorHistResult/newsongdoCCTV/hj2_2_hist_out.json') as json_file3:
    json_data3 = json.load(json_file3)
with open('./colorHistResult/newsongdoCCTV/hj3_1_hist_out.json') as json_file4:
    json_data4 = json.load(json_file4)
with open('./colorHistResult/newsongdoCCTV/hj3_2_hist_out.json') as json_file5:
    json_data5 = json.load(json_file5)
with open('./colorHistResult/newsongdoCCTV/my1_hist_out.json') as json_file6:
    json_data6 = json.load(json_file6)
with open('./colorHistResult/newsongdoCCTV/my2_1_hist_out.json') as json_file7:
    json_data7 = json.load(json_file7)
with open('./colorHistResult/newsongdoCCTV/my2_2_hist_out.json') as json_file8:
    json_data8 = json.load(json_file8)
with open('./colorHistResult/newsongdoCCTV/my3_1_hist_out.json') as json_file9:
    json_data9 = json.load(json_file9)
with open('./colorHistResult/newsongdoCCTV/my3_2_hist_out.json') as json_file10:
    json_data10 = json.load(json_file10)
with open('./colorHistResult/newsongdoCCTV/ys1_hist_out.json') as json_file11:
    json_data11 = json.load(json_file11)
with open('./colorHistResult/newsongdoCCTV/ys2_1_hist_out.json') as json_file12:
    json_data12 = json.load(json_file12)
with open('./colorHistResult/newsongdoCCTV/ys2_2_hist_out.json') as json_file13:
    json_data13 = json.load(json_file13)
with open('./colorHistResult/newsongdoCCTV/ys3_1_hist_out.json') as json_file14:
    json_data14 = json.load(json_file14)
with open('./colorHistResult/newsongdoCCTV/ys3_2_hist_out.json') as json_file15:
    json_data15 = json.load(json_file15)
with open('./colorHistResult/newsongdoCCTV/bf1_1_hist_out.json') as json_file16:
    json_data16 = json.load(json_file16)
with open('./colorHistResult/newsongdoCCTV/bf1_2_hist_out.json') as json_file17:
    json_data17 = json.load(json_file17)
with open('./colorHistResult/newsongdoCCTV/bf1_3_hist_out.json') as json_file18:
    json_data18 = json.load(json_file18)
with open('./colorHistResult/newsongdoCCTV/bf1_4_hist_out.json') as json_file19:
    json_data19 = json.load(json_file19)
with open('./colorHistResult/newsongdoCCTV/bf2_1_hist_out.json') as json_file20:
    json_data20 = json.load(json_file20)
with open('./colorHistResult/newsongdoCCTV/bf2_2_hist_out.json') as json_file21:
    json_data21 = json.load(json_file21)
with open('./colorHistResult/newsongdoCCTV/bf3_1_hist_out.json') as json_file22:
    json_data22 = json.load(json_file22)
with open('./colorHistResult/newsongdoCCTV/bf3_2_hist_out.json') as json_file23:
    json_data23 = json.load(json_file23)
with open('./colorHistResult/newsongdoCCTV/js1_1_hist_out.json') as json_file24:
    json_data24 = json.load(json_file24)
with open('./colorHistResult/newsongdoCCTV/js1_2_hist_out.json') as json_file25:
    json_data25 = json.load(json_file25)
with open('./colorHistResult/newsongdoCCTV/js2_1_hist_out.json') as json_file26:
    json_data26 = json.load(json_file26)
with open('./colorHistResult/newsongdoCCTV/js2_2_hist_out.json') as json_file27:
    json_data27 = json.load(json_file27)
with open('./colorHistResult/newsongdoCCTV/js3_1_hist_out.json') as json_file28:
    json_data28 = json.load(json_file28)
with open('./colorHistResult/newsongdoCCTV/js3_2_hist_out.json') as json_file29:
    json_data29 = json.load(json_file29)

while(True):
    global k
    if len(json_data1['det'])> len(json_data2['det']):
        k = len(json_data2['det'])
    else:
        k = len(json_data1['det'])
    #print("what is k:",k)
    # print("what is hst_h:",json_data1['det'][i]['hist_h'])
    # print("what is hst_h:",json_data2['det'][i]['hist_h'])

    # try:
    #dtype=float32
    cmph = cv2.compareHist(cv2.UMat(np.array(json_data1['det'][i]['hist_h'], dtype=float32)), cv2.UMat(np.array(json_data2['det'][i]['hist_h'],dtype=float32)),cv2.HISTCMP_CORREL)
    cmps = cv2.compareHist(cv2.UMat(np.array(json_data1['det'][i]['hist_s'], dtype=float32)), cv2.UMat(np.array(json_data2['det'][i]['hist_s'],dtype=float32)),cv2.HISTCMP_CORREL)
    #cmpv = cv2.compareHist(cv2.UMat(np.array(json_data1['det'][i]['hist_v'], dtype=float32)), cv2.UMat(np.array(json_data2['det'][i]['hist_v'],dtype=float32)),cv2.HISTCMP_CORREL)
    # BEST: HISTCMP_CORREL option
    
    # cmps = cv2.compareHist(json_data1['det'][i]['hist_s'],json_data2['det'][i]['hist_s'],cv2.HISTCMP_INTERSECT)
    # cmpv = cv2.compareHist(json_data1['det'][i]['hist_v'],json_data2['det'][i]['hist_v'],cv2.HISTCMP_INTERSECT)
    
    if( ( abs(cmph)>=0.5 or ( abs(cmph)>=0.35) and (abs(cmps))>=0.2 ) ):
        s = s + 1

    file_data1[i+1]={'cmph':abs(cmph), 'cmps':abs(cmps)}
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
        file_data1['final']={'OverThreshold':s, 'Ratio': int(z * 100), 'Frame': k}
        break

#   # cv2.imshow("Image window", cv_image)
    cv2.waitKey(50)

with open('./FinalCompareResult/CMP_Hist_hj1_hj21.json','w' ) as make_file:
    json.dump(file_data1,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_hj22.json','w' ) as make_file:
    json.dump(file_data2,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_hj31.json','w' ) as make_file:
    json.dump(file_data3,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_hj32.json','w' ) as make_file:
    json.dump(file_data4,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_my1.json','w' ) as make_file:
    json.dump(file_data5,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_my21.json','w' ) as make_file:
    json.dump(file_data6,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_my22.json','w' ) as make_file:
    json.dump(file_data7,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_my31.json','w' ) as make_file:
    json.dump(file_data8,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_my32.json','w' ) as make_file:
    json.dump(file_data9,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_ys1.json','w' ) as make_file:
    json.dump(file_data10,make_file,ensure_ascii=False, indent=4)  
with open('./FinalCompareResult/CMP_Hist_hj1_ys21.json','w' ) as make_file:
    json.dump(file_data11,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_ys22.json','w' ) as make_file:
    json.dump(file_data12,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_ys31.json','w' ) as make_file:
    json.dump(file_data13,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_ys32.json','w' ) as make_file:
    json.dump(file_data14,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_bf11.json','w' ) as make_file:
    json.dump(file_data15,make_file,ensure_ascii=False, indent=4)  
with open('./FinalCompareResult/CMP_Hist_hj1_bf12.json','w' ) as make_file:
    json.dump(file_data16,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_bf13.json','w' ) as make_file:
    json.dump(file_data17,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_bf14.json','w' ) as make_file:
    json.dump(file_data18,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_bf21.json','w' ) as make_file:
    json.dump(file_data19,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_bf22.json','w' ) as make_file:
    json.dump(file_data20,make_file,ensure_ascii=False, indent=4)  
with open('./FinalCompareResult/CMP_Hist_hj1_bf31.json','w' ) as make_file:
    json.dump(file_data21,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_bf32.json','w' ) as make_file:
    json.dump(file_data22,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_js11.json','w' ) as make_file:
    json.dump(file_data23,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_js12.json','w' ) as make_file:
    json.dump(file_data24,make_file,ensure_ascii=False, indent=4)    
with open('./FinalCompareResult/CMP_Hist_hj1_js21.json','w' ) as make_file:
    json.dump(file_data25,make_file,ensure_ascii=False, indent=4)  
with open('./FinalCompareResult/CMP_Hist_hj1_js22.json','w' ) as make_file:
    json.dump(file_data26,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_js31.json','w' ) as make_file:
    json.dump(file_data27,make_file,ensure_ascii=False, indent=4)
with open('./FinalCompareResult/CMP_Hist_hj1_js32.json','w' ) as make_file:
    json.dump(file_data28,make_file,ensure_ascii=False, indent=4)   
