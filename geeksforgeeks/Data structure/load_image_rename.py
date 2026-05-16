import cv2
import glob
import os

import natsort

from PIL import Image

src_dir = "D:\FSC Camera\FSC231_Stereo_Dataset\left"
dst_dir = "D:\FSC Camera\FSC231_Stereo_Dataset\processed"
images = os.listdir(src_dir)
# print(images)
# print(natsort.natsorted(images,reverse=False))
sorted_file_name = natsort.natsorted(images,reverse=False)
print(sorted_file_name)

# # renaming
# for i in range(len(sorted_file_name)):
#     f = os.path.splitext(sorted_file_name[i-1])
#     f = sorted_file_name[i-1].split("_")
#     print("splitted:", f)
#     os.rename(os.path.join(src_dir, sorted_file_name[i-1]), os.path.join(src_dir, str(i).zfill(6) + '.png'))
#
#

# # # maintain quality
for i in range(len(sorted_file_name)):
    load_image = os.path.join(src_dir, sorted_file_name[i])
    imgs = Image.open(load_image)
    resized_image = imgs.resize((512, 512))
    f = os.path.splitext(sorted_file_name[i])
    # f = sorted_file_name[i].split(".")
    resized_image.save(os.path.join(dst_dir, f[0]+'.png'))
    # resized_image.save(os.path.join(dst_dir, sorted_file_name[i]))
print("Done")

# # cropped
#
# for i in range(1, len(sorted_file_name)):
#     img = Image.open(os.path.join(src_dir, sorted_file_name[i]))
#     new_image = img.resize((1920, 1080))
#     new_image.save(os.path.join(os.path.join(dst_dir, sorted_file_name[i])))
# print("Done cropping")