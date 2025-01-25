import numpy as np
import cv2


def discard_extremes(I, percentage: int):
    num_image = len(I)
    # sort intensities for each pixels
    I_sorted = np.sort(I)
    num_to_discard = int(num_image * percentage / 100)
    for i in range(num_to_discard):
        I_sorted[i] = 0  # Discard darkest values
        I_sorted[-(i + 1)] = 0  # Discard brightest values
    return I_sorted


def pms(images, L_list, percentage):
    print("PMS algorihtm")
    L = np.array(L_list)  # convert L_list into np array
    L_transpose = L.T  # transpose of L
    height, weight = images[0].shape[:2]
    print(height, weight)
    # intilize image normal and image albedo
    image_normal = np.zeros((height, weight, 3))
    image_albedo = np.zeros((height, weight, 3))

    # intilize intensity
    size_L = len(L_list)
    I = np.zeros((size_L, 3))
    print(weight)
    for x in range(weight):
        for y in range(height):
            for i in range(len(images)):

                I[i] = images[i][y][x]
            # handling shadow and outlier
            I = discard_extremes(I, percentage)
            # solve surface normal
            temp1 = np.linalg.inv(np.dot(L_transpose, L))  # (S^T . S)^-1
            temp2 = np.dot(L_transpose, I)  # S^T . I
            N = np.dot(temp1, temp2).T
            # compute albedo rho
            rho = np.linalg.norm(N, axis=1)
            image_albedo[y][x] = rho

            # compute rgb using luminosity
            N_gray = N[0] * 0.0722 + N[1] * 0.7152 + N[2] * 0.2126
            Nnorm = np.linalg.norm(N)
            if Nnorm == 0:
                continue
            image_normal[y][x] = N_gray / Nnorm
    # Normalize and visualize the normal image
    image_temp = image_normal
    image_normal_rgb = ((image_normal * 0.5 + 0.5) * 255).astype(np.uint8)
    image_normal_rgb = cv2.cvtColor(image_normal_rgb, cv2.COLOR_BGR2RGB)

    image_albedo = (image_albedo / np.max(image_albedo) * 255).astype(np.uint8)
    print(image_albedo)

    # Re-rendered image
    view_dir = np.array([0, 0, 1])  # View direction
    light_dir = view_dir  # Illumination direction is the same as the view direction
    light_dir = light_dir / np.linalg.norm(
        light_dir
    )  # Normalize the light direction if necessary
    Re_rendered_image = re_render(image_normal, image_albedo, light_dir)
    return image_normal, image_albedo, image_normal_rgb, Re_rendered_image


def re_render(image_normal, image_albedo, light_dir):
    height, width, _ = image_normal.shape
    re_rendered_image = np.zeros((height, width, 3), dtype=np.float32)  # RGB output
    light_dir = light_dir / np.linalg.norm(light_dir)
    print("Re-rendering image")
    for y in range(height):
        for x in range(width):
            normal = image_normal[y][x]
            albedo = image_albedo[y][x]

            normal_norm = np.linalg.norm(normal)
            if normal_norm != 0:
                normal = normal / normal_norm
            dot_product = np.dot(light_dir, normal)
            dot_product = max(dot_product, 0)
            re_rendered_image[y][x] = albedo * dot_product
    re_rendered_image = (re_rendered_image).astype(np.uint8)

    return re_rendered_image
