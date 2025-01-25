# Photometric Stereo for 3D Surface Reconstruction

## Overview

This repository implements **Photometric Stereo**, a technique for reconstructing the 3D shape of an object by analyzing multiple images taken from different viewpoints under varying lighting conditions. By exploiting the intensity variations at each pixel across these images, the algorithm estimates surface normals and albedo, enabling the reconstruction of surface geometry. This method is particularly useful in scenarios where only a sequence of images with different light sources is available, providing an efficient way to capture the 3D structure of an object without the need for depth sensors or 3D scanning equipment.

Photometric Stereo has widespread applications in computer vision, 3D modeling, robotics, and augmented reality, where high-quality, fine-grained surface geometry is needed from ordinary images.

### Key Features:
- **Estimation of Surface Normals**: The method uses pixel intensity variations across multiple images to estimate the surface orientation of the object at each point.
- **Albedo Recovery**: The algorithm estimates the albedo (reflectivity) of the object surfaces, crucial for realistic rendering and scene understanding.
- **Surface Re-rendering**: Using the recovered surface properties (normals and albedo), the system re-renders the object from novel perspectives or under different lighting conditions.

## Introduction

### The Principle of Photometric Stereo

The core idea behind Photometric Stereo is that by capturing multiple images of an object under different lighting conditions, we can use the intensity values of pixels at each point across these images to infer the surface normal vectors at those points. The relationship between the light source, surface orientation, and pixel intensity is governed by the **Lambertian Reflection Model**, which assumes that the surface reflects light diffusely.

By solving the system of equations formed by the Lambertian reflection model for each pixel across multiple images, we can obtain the surface normals, which describe the orientation of the surface at each point. Once the normals are estimated, we can use them to recover additional properties, such as the surface albedo and reconstruct the object's 3D geometry.

#### Mathematical Formulation:
Given an image sequence of an object under varying lighting conditions, the intensity value at pixel $(x, y)$ for light source $i$ is given by:

$$
I_i(x, y) = \rho(x, y) \cdot \mathbf{n}(x, y) \cdot \mathbf{l_i}
$$


$$
I_i(x, y) = \rho(x, y) \cdot \mathbf{n}(x, y) \cdot \mathbf{l_i}
$$

Where:
- $\rho(x, y)$ is the albedo (reflectivity) of the surface at pixel $(x, y)$,
- $\mathbf{n}(x, y)$ is the surface normal at pixel $(x, y)$,
- $\mathbf{l_i}$ is the direction vector of the light source $i$.


This equation is solved for each pixel using images captured under different light source directions to estimate the normal vector \( \mathbf{n}(x, y) \) and the albedo \( \rho(x, y) \).

### Challenges:
- **Shadow and Highlight Handling**: The presence of shadows and highlights can cause significant outliers in the intensity measurements, making the estimation of surface normals more difficult. The implementation uses robust outlier detection techniques to mitigate the effect of such artifacts.
- **Ambiguity in Surface Normal Estimation**: A single image cannot distinguish between surface orientations that are mirror images of each other, leading to ambiguities. Using multiple images with different lighting sources helps resolve this issue.

### Figure 1: Principle of Photometric Stereo

The diagram below illustrates how multiple images under different lighting conditions are used to recover surface normals and albedo.

![Photometric Stereo Principle](res/bearPNG.png) 
![Photometric Stereo Principle](res/buddhaPNG.png) 
![Photometric Stereo Principle](res/catPNG.png) 
![Photometric Stereo Principle](res/potPNG.png) 
## Setup

To run the project, you need to set up the appropriate environment and install the required dependencies. Follow the steps below to get started:

### Step 1: Create a Conda Environment

It is recommended to use a **Conda environment** to ensure that all dependencies are isolated and compatible.

```bash
conda create --name ps python=3.9
conda activate ps
