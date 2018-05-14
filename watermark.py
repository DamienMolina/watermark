from PIL import Image
import os
import glob

mask = Image.open('mask.png')

area = (50, 50)

name_folder_in = "photos_in"
name_folder_in = input("What's the name of the folder of the photos you want to watermark?")
name_folder_out = "watermarked_photos"

if not os.path.exists(name_folder_out):
    os.makedirs(name_folder_out)
if not os.path.exists(name_folder_out+"/"+name_folder_in):
    os.makedirs(name_folder_out+"/"+name_folder_in)

list_files = []
file_type = ["*.jpg", "*.JPG"]
for i in file_type:
    param = "{}/{}".format(name_folder_in, i)
    list_files.extend(glob.glob(param))
for i in list_files:
    im_original = Image.open(i)
    im_original.paste(mask, area, mask)
    path_out = "{}/{}".format(name_folder_out,i)
    print(path_out)
    im_original.save(path_out)
