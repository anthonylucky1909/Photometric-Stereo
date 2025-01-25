import random
import cv2
import re
import os
import numpy as np
from numpy import loadtxt


def numerical_sort(value):
    nums = re.compile(r"(\d+)")
    parts = nums.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


# convert image to vector
def imread_image(list_object=None, I=None, flag=-1, scale=1):
    # checking list object
    if list_object == None:
        print("The list of object is empty")
        exit()
    # list of images name
    image_names = list_object
    # sorted file paths numerical
    image_names = sorted(image_names, key=numerical_sort)
    image_list = []

    # reading images and normalize images
    for i, path in enumerate(image_names):
        image = cv2.resize(cv2.imread(path, flag), None, fx=scale, fy=scale)
        # normalize image
        if np.any(I):
            image = image / I[i]
        image_list.append(image)
    return image_list


# loading images and convert image from image into vector (images + mask)
def loader_dataset(object: str):
    data_path = "./pmsData/"
    # loading light direction
    L_direction = loadtxt(data_path + object + "/light_directions.txt")
    # loading light intensities
    intensities = loadtxt(data_path + object + "/light_intensities.txt")
    # load file name
    file = loadtxt(data_path + object + "/filenames.txt", dtype=str)
    filenames = []
    for i in range(len(file)):
        temp = data_path + object + "/" + file[i]
        filenames.append(temp)
    # transform image into vector
    images = imread_image(filenames, I=intensities)
    # loading mask image into vector
    mask = imread_image([data_path + object + "/mask.png"])[0]
    return images, mask, L_direction


if __name__ == "__main__":
    # testing
    object = ["bearPNG", "catPNG", "buddhaPNG", "potPNG"]  # object in pmsData
    images, mask, L_direction = loader_dataset(
        object=object[0]
    )  # loadoing object bearPNG
    