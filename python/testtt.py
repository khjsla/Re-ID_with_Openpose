import numpy as np
import cv2
from PIL import Image
import numpy as np
import json
import math
import os, glob
from math import *
import math

import scipy.stats
from scipy.stats import norm
import matplotlib.pyplot as plt

file_data = dict()

point1213 = 0
point111 = 0
point89 = 0
point18 = 0
point910 = 0
point1112 = 0
i = 0

def tips_range(n, start, end = 0):
    return start <= n <= end if end >= start else end <= n <= start

input_n = '1_my1'

# 1_my1_r_99
# 1_hj1_r_95
# 1_sbf1_r_90
# 1_sjs1_r_95

# 2_hj1
# 2_sjs1
# 2_my1
# 2_sbf1s

# 3_hj1
# 3_sjs1
# 3_my1
# 3_sbf1

# point = '_99'
file_n = '../JSONmade/realcp/' + str(input_n) + '.json'
print("******* find {0} *******".format(input_n))
with open(file_n) as json_file:
    orig_data = json.load(json_file)

frame_id = orig_data['det']['frame_n']
ratio_1213 = orig_data['det']['dist1213']
ratio_111 = orig_data['det']['dist111']
ratio_89 = orig_data['det']['dist89']
ratio_18 = orig_data['det']['dist18']
ratio_910 = orig_data['det']['dist910']
ratio_1112 = orig_data['det']['dist1112']

def check():
    file_list = glob.glob('../JSONmade/realcp/*.json')
    # print(file_list)
    file_lists = len(file_list)
    # print(file_lists)
    for ll in range(0, file_lists):
        new_name = file_list[int(ll)].split('/')[-1]
        # print(new_name)
        i = 0
        with open(file_list[ll]) as json_file:
            # print(file_list[ll])
            json_data = json.load(json_file)
        frame_id = json_data['det']['frame_n']
        r_1213 = json_data['det']['dist1213']
        r_111 = json_data['det']['dist111']
        r_89 = json_data['det']['dist89']
        r_18 = json_data['det']['dist18']
        r_910 = json_data['det']['dist910']
        r_1112 = json_data['det']['dist1112']

        if tips_range(r_1213[0], ratio_1213[0], ratio_1213[2]) or tips_range(r_1213[1], ratio_1213[0], ratio_1213[2]) or tips_range(r_1213[2], ratio_1213[0], ratio_1213[2]):
            point_1213 = True
        else:
            point_1213 = False
        if tips_range(r_111[0], ratio_111[0], ratio_111[2]) or tips_range(r_111[1], ratio_111[0], ratio_111[2]) or tips_range(r_111[2], ratio_111[0], ratio_111[2]):
            point_111 = True
        else:
            point_111 = False
        if tips_range(r_89[0], ratio_89[0], ratio_89[2]) or tips_range(r_89[1], ratio_89[0], ratio_89[2]) or tips_range(r_89[2], ratio_89[0], ratio_89[2]):
            point_89 = True
        else:
            point_89 = False
        if tips_range(r_18[0], ratio_18[0], ratio_18[2]) or tips_range(r_18[1], ratio_18[0], ratio_18[2]) or tips_range(r_18[2], ratio_18[0], ratio_18[2]):
            point_18 = True
        else:
            point_18 = False
        if tips_range(r_910[0], ratio_910[0], ratio_910[2]) or tips_range(r_910[1], ratio_910[0], ratio_910[2]) or tips_range(r_910[2], ratio_910[0], ratio_910[2]):
            point_910 = True
        else:
            point_910 = False
        if tips_range(r_1112[0], ratio_1112[0], ratio_1112[2]) or tips_range(r_1112[1], ratio_1112[0], ratio_1112[2]) or tips_range(r_1112[2], ratio_1112[0], ratio_1112[2]):
            point_1112 = True
        else:
            point_1112 = False
        
        p_list = [point_111, point_1112, point_89, point_18, point_1213, point_910]
        for p in p_list:
            if p == True:
                i = i+1
        # if new_name
        if i >= 5:
            # print(new_name)
            if input_n + '.json' == new_name:
                pass
            else: color(new_name, json_data["time"])
            # print("TRUE")
        # else:
            # print('{0}: False'.format(file_list[ll]))
            # print(i)

def color(color_name, time):
    color_path = '../JSONmade/result/' + input_n + '_' + color_name
    with open(color_path) as color_file:
        color_data = json.load(color_file)
    color_score = color_data['final']['Ratio']
    if color_score >= 25:
        where = color_name.split('_')[0]
        file_data['camera'] = {}
        print('{0}'.format(color_name))
        # print(time)
        print('CAM{0}_{1}'.format(where, time)) 

check()

# print(dist_111)

# dist_1213 = 
