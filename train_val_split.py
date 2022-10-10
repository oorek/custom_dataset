import os
from glob import glob
import shutil
from sklearn.model_selection import train_test_split

image_files = glob('D:/roadmark_unbalanced_mixed/new_roadmark_img/*.png')

images = [name.replace('.png', '') for name in image_files]

train_names, test_names = train_test_split(images, test_size = 0.2, random_state=42, shuffle=True)

val_names, test_names = train_test_split(test_names, test_size=0.5, random_state=42, shuffle=True)

def batch_move_files(file_list, img_source_path, txt_source_path, img_destination_path, txt_destination_path):
    for file in file_list:
        image = file.split('/')[-1] + '.png'
        txt = file.split('/')[-1] + 'txt'

        shutil.copy(os.path.join(img_source_path, image), img_destination_path)
        shutil.copy(os.path.join(txt_source_path, txt), txt_destination_path)
    return

img_source_dir = 'D:/roadmark_unbalanced_mixed/new_roadmark_img/'
txt_source_dir = 'D:/roadmark_unbalanced_mixed/new_roadmark_txt/'

img_train_dir = 'D:/roadmark_unbalanced_mixed/new_custom_dataset/train/images'
txt_train_dir = 'D:/roadmark_unbalanced_mixed/new_custom_dataset/train/labels'
img_val_dir = 'D:/roadmark_unbalanced_mixed/new_custom_dataset/val/images'
txt_val_dir = 'D:/roadmark_unbalanced_mixed/new_custom_dataset/val/labels'
img_test_dir = 'D:/roadmark_unbalanced_mixed/new_custom_dataset/test/images'
txt_test_dir = 'D:/roadmark_unbalanced_mixed/new_custom_dataset/test/labels'

batch_move_files(train_names, img_source_dir, txt_source_dir, img_train_dir, txt_train_dir)
batch_move_files(val_names, img_source_dir, txt_source_dir,  img_val_dir, txt_val_dir)
batch_move_files(test_names, img_source_dir, txt_source_dir, img_test_dir, txt_test_dir)