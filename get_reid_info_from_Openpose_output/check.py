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
ll = 0

file_list = glob.glob('./colorHistResult/newsongdoCCTV/*.json')
file_lists = len(file_list)
for ll in file_list:
    print(ll)