from PIL import Image
import os
from typing import List
import numpy as np

def list_folder(path_to_dataset):
    folders = os.listdir(path_to_dataset)
    return folders

def all_images(path_to_dataset:str) -> List:
    list_img = []
    folders = list_folder(path_to_dataset)
    for folder in folders:
        imgs = os.listdir(os.path.join(path_to_dataset, folder))
        for img in imgs:
            list_img.append(os.path.join(path_to_dataset, folder, img))
    return list_img

def read_img(list_path_imgs):
    count = 0 
    for img_path in list_path_imgs:
        image = Image.open(img_path)
        image = np.array(image)
        if len(image.shape) == 2:
            img_3_channels = np.stack((image, )*3, axis=-1)
            image = Image.fromarray(img_3_channels)
            image = image.convert("RGB")
            image.save(img_path)
            count +=1
            continue

        if image.shape[2] == 4:
            image = image[...,:3]
            image = Image.fromarray(image)
            image = image.convert("RGB")
            image.save(img_path)
            count += 1
    print('Change png file ', count)

    


list_imgs = all_images('./dataset_256')
read_img(list_imgs)


