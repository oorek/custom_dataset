from distutils.log import error
import json
import os
import pdb

#file_path = "./c_validation_1280_720_daylight_1/"
cur_dir = os.getcwd()
file_path = "C:/Users/a/annotation/c_validation_1280_720_daylight_1"
os.chdir(file_path)
file_list = os.listdir()
os.chdir(cur_dir)
#cnt=0
for filename in file_list:
    file_name = os.path.splitext(filename)[0]
    with open(filename, "r") as original:
        print(filename)
        wf = open("./traffic_sign_txt/%s.txt" % file_name, 'w')
        original = json.load(original)
        for el in original["annotation"]:
            tmp = True
            #pdb.set_trace()
            dict_keys = el.keys()
            if "class" in dict_keys:
                if (el["class"] == "traffic_light") :
                    if "attribute" in dict_keys:
                        if (el["attribute"][0]["red"] == "on"):
                            sign = 0
                        elif (el["attribute"][0]["yellow"] == "on"):
                            sign = 1
                        elif (el["attribute"][0]["green"] == "on"):
                            sign = 2
                        else:
                            tmp = False
                            pass
                        if tmp == True:
                            wf.write("%d " % sign)
                    else:
                        raise error
                elif (el["class"] == "traffic_sign"):
                    if "type" in dict_keys:
                        if (el["type"] == "restriction"):
                            #red +=1
                            sign = 3
                        elif (el["type"] == "caution"):
                            #yellow+=1
                            sign = 4
                        elif (el["type"] == "instruction"):
                            #green+=1
                            sign = 5
                        wf.write("%d " % sign)
                    else:
                        tmp = False
                        pass
                        #cnt+=1
                        #wf.write("7 ")
                else:
                    #cnt+=1
                    tmp = False
                if tmp == True:
                    center_x = (el["box"][0] + el["box"][2]) / 2
                    center_y = (el["box"][1] + el["box"][3]) / 2
                    width = (el["box"][2] - el["box"][0])
                    height = (el["box"][3] - el["box"][1])
                    if center_x > 1280 or center_y > 720 or center_x < 0 or center_y < 0:
                        raise error
                    if width > 1280 or height > 720 or width < 0 or height < 0:
                        raise error
                    wf.write("%f %f %f %f\n" % (center_x/1280, center_y/720, width/1280, height/720))
        wf.close()
#print(cnt)