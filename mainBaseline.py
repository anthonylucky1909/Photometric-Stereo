import cv2
import numpy as np
from load_datasetdir import loader_dataset
from vecToimg import vecToimage
from pms import pms


def main() -> None:
    object = ["bearPNG", "buddhaPNG", "catPNG", "potPNG"]  # object in pmsData
    for obj in object:
        print("Processing with images : ", obj)
        images, mask, L_direction = loader_dataset(obj)
        # after that applying mask into the images
        for i, image in enumerate(images):
            images[i] = cv2.bitwise_and(image, image, mask=mask)
            i += 1
        images = np.array(images)
        # applying algorithm and addressing Dealing with shadows and highlights
        image_normal, image_albedo, image_normal_rgb, image_render = pms(
            images, L_direction, 10
        )
        # saving images in res directory
        vecToimage(
            images, image_normal, image_albedo, image_normal_rgb, image_render, str(obj)
        )

    return


if __name__ == "__main__":
    main()
