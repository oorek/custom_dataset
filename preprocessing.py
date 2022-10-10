from distutils.log import error
import json
import os
import pdb
import shutil

cur_path = os.getcwd()

image_file_path = "./IMAGE/"
os.chdir(image_file_path)
image_file_list = os.listdir()

os.chdir(cur_path)
txt_file_path = "./roadmark3_txt/"
os.chdir(txt_file_path)
txt_file_list = os.listdir()

os.chdir(cur_path)

copy_img = "./new_roadmark_img/"
copy_txt = "./new_roadmark_txt/"

for txt in txt_file_list:
    dir = str(txt_file_path+txt)
    size = os.path.getsize(dir)
    isempty = size == 0
    if isempty == False:
        shutil.copy(dir, copy_txt)

os.chdir(cur_path)
new_txt_file_path = os.chdir(copy_txt)
new_txt_file_list = os.listdir(new_txt_file_path)
len = len(new_txt_file_list)
os.chdir(cur_path)
tmp = 0
count=0
for img in image_file_list:
    image_filename = os.path.splitext(img)[0]
    dir = str(image_file_path + img)
    for i in range(tmp, len):
        txt_filename = os.path.splitext(new_txt_file_list[i])[0]
        if image_filename == txt_filename:
            print(count)
            count+=1
            shutil.copy(dir, copy_img)