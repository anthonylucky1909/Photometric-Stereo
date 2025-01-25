import matplotlib.pyplot as plt
import numpy as np


def vecToimage(imgs, image_normal, img_albedo, img_normal_rgb, image_render, object):
    plt.figure(figsize=(30, 5))
    # Subplot 1: Example image with one light source
    plt.subplot(1, 5, 1)
    img = (imgs[1] - np.min(imgs[1])) / (
        np.max(imgs[1]) - np.min(imgs[1])
    )  # Normalizing image between 0-1 for visualization
    plt.imshow(img)
    plt.title("Example image with one light source")
    plt.xticks([])
    plt.yticks([])
    # addition
    plt.subplot(1, 5, 2)
    plt.imshow(image_normal)
    plt.title("Image normal")
    plt.xticks([])
    plt.yticks([])

    # Subplot 3: Image Albedo
    plt.subplot(1, 5, 3)
    plt.imshow(img_albedo)
    plt.title("Image Albedo")
    plt.xticks([])
    plt.yticks([])

    # Subplot 4: Surface Normals
    plt.subplot(1, 5, 4)
    plt.imshow(img_normal_rgb)
    plt.title("Surface Normals")
    plt.xticks([])
    plt.yticks([])

    # subplot 5: re-render image
    # Subplot 4: Surface Normals
    plt.subplot(1, 5, 5)
    plt.imshow(image_render)
    plt.title("Re-rendered Image")
    plt.xticks([])
    plt.yticks([])

    # Save the figure
    plt.savefig(
        "res/" + object + ".png", dpi=300, bbox_inches="tight"
    )  # Save as a high-quality image
    # Show the figure
    # plt.show()
