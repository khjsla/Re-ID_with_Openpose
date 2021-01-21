import numpy as np
import cv2
from PIL import Image
import numpy as np
from math import*
import json
import math
import os, glob
import codecs, json 

file_data = dict()
i = 0
cnt = 0
n = 1
num = 0

file_list = glob.glob('./songdoCCTV/json/js/3/2/*.json')
file_lists = len(file_list)
file_data['det'] = []
for ll in range(0, file_lists):
    
    file_name = './songdoCCTV/json/js/3/2/3_sjs2_' + str(ll+1) + '.json'
    with open(file_name) as json_file:
        file_data['det'].append({'frame_id' : int(str(ll+1)) })
        kk = 0
        json_data = json.load(json_file)
        json_roi = json_data['people']
        if not json_roi:
            pass
        else:
            global nn
            name = 0
            while name < len(json_data['people'][0]['pose_keypoints_2d']):

                if(name == 0):
                    globals()['p_0'] = []
                    nn = globals()['p_0']
                if (name)%3 == 2 and name + 1 < len(json_data['people'][0]['pose_keypoints_2d']):
                    kk = kk + 1
                    globals()['p_' + str(kk)] = []
                    nn = globals()['p_' + str(kk)]
                    name = name + 1

                if name != len(json_data['people'][0]['pose_keypoints_2d'])-1:
                    nn.append(np.array(json_data['people'][0]['pose_keypoints_2d'][name]))
                name = name + 1

            if  p_1[0] and p_8[0] and p_11[0] and p_1[1] and p_8[1] and p_11[1] != 0:
                file_data['det'][ll]['people'] = {
                '1' : [float(p_1[0]), float(p_1[1])]
                ,'8' : [float(p_8[0]), float(p_8[1])]
                ,'11' : [float(p_11[0]), float(p_11[1])]
                }

with open('./colorROIsetting/songdoCCTV/js3_2.json','w' ) as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent=3)
