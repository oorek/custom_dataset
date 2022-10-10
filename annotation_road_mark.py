from distutils.log import error
import json
import os
import pdb

file_path = "./roadmark_2/"
os.chdir(file_path)
file_list = os.listdir()

def get_bbox(el):
    center_x = el['bbox'][0] + (el['bbox'][2] / 2)
    center_y = el['bbox'][1] + (el['bbox'][3] / 2)
    width = el['bbox'][2]
    height = el['bbox'][3]
    if center_x > 0 and center_x < 1920 and center_y > 0 and center_y < 1080:
        return center_x, center_y, width, height
    else:
        return (-1,)

for filename in file_list:
    file_name = os.path.splitext(filename)[0]
    with open(filename, "r", encoding="UTF-8") as original:
        print(filename)
        original = json.load(original)
        wf = open("../output_roadmark3/%s.txt" % file_name, 'w')   
        for el in original["annotations"]:
            tmp = True
            T = tuple
            dict_keys = el.keys()
            if 'category_id' in dict_keys:
                if 'bbox' in dict_keys:
                    if el['bbox'][0] > 0 and el['bbox'][1] > 0 and el['bbox'][2] > 0 and el['bbox'][3] > 0:
                        if el['bbox'][0] < 1920 and el['bbox'][1] < 1080 and el['bbox'][2] < 1920 and el['bbox'][3] < 1080:
                            T = get_bbox(el)
                            tmp = True
                            if T[0] == -1:
                                print("here")
                                tmp = False
                        else:
                            tmp = False
                    else:
                        tmp = False
                else:
                    #print("no bbox")
                    tmp = False
                    #raise error
                if tmp == True:
                    if el['category_id'] == 394:
                        sign = 0
                    elif el['category_id'] == 395:
                        sign = 1
                    elif el['category_id'] == 396:
                        sign = 2
                    elif el['category_id'] == 397:
                        sign = 3
                    elif el['category_id'] == 398:
                        sign = 4
                    elif el['category_id'] == 399:
                        sign = 5
                    elif el['category_id'] == 400:
                        sign = 6
                    elif el['category_id'] == 401:
                        sign = 7
                    elif el['category_id'] == 402:
                        sign = 8
                    elif el['category_id'] == 403:
                        sign = 9
                    elif el['category_id'] == 404:
                        sign = 10
                    elif el['category_id'] == 405:
                        sign = 11
                    elif el['category_id'] == 412:
                        sign = 12
                    elif el['category_id'] == 413:
                        sign = 13
                    elif el['category_id'] == 414:
                        sign = 14
                    elif el['category_id'] == 424:
                        sign = 15
                    elif el['category_id'] == 429:
                        sign = 16
                    else:
                        tmp = False
                    if tmp == True:                  
                        wf.write("%d " % sign)
                        #print(T[0], T[1], T[2], T[3])
                        wf.write("%f %f %f %f\n" % (T[0]/1920, T[1]/1080, T[2]/1920, T[3]/1080))
            else:
                #print("no category id")
                raise error
        wf.close()