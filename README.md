# 🌟 Photometric Stereo for 3D Surface Reconstruction

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?logo=python&style=flat-square)](https://www.python.org/)
[![Release](https://img.shields.io/github/v/release/anthonylucky1909/Photometric-Stereo?style=flat-square)](https://github.com/anthonylucky1909/Photometric-Stereo/releases)
[![Build](https://img.shields.io/github/actions/workflow/status/anthonylucky1909/Photometric-Stereo/ci.yml?branch=main&style=flat-square)](https://github.com/anthonylucky1909/Photometric-Stereo/actions)
[![Stars](https://img.shields.io/github/stars/anthonylucky1909/Photometric-Stereo?style=flat-square)](https://github.com/anthonylucky1909/Photometric-Stereo/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)


## 🎯 Overview
This project implements **Photometric Stereo**, a classic computer vision technique for recovering the **3D shape** of objects from 2D images taken under different lighting conditions.  
It estimates both **surface normals** and **albedo**, enabling realistic **3D reconstruction** without special sensors.  

---

## ✨ Features
- 🧭 Estimate **surface normals**  
- 🌈 Recover **albedo (reflectivity)**  
- 🎥 Re-render objects under new lighting  

---

## ⚙️ Quick Setup
```bash
# Create environment
conda create --name ps python=3.9
conda activate ps

# Install dependencies
pip install -r requirements.txt

# Run example
python main.py --data ./data/bear --output ./results/bear
```

---

## 🖼️ Results
Some example reconstructions:  

![Bear](res/bearPNG.png)  
![Buddha](res/buddhaPNG.png)  
![Cat](res/catPNG.png)  
![Pot](res/potPNG.png)  

---

## 📜 References
- R. Woodham, *Photometric Method for Determining Surface Orientation from Multiple Images*  
- Horn, B.K.P., *Robot Vision*, MIT Press  

---

## 🤝 Contributing
Contributions, issue reports, and feature requests are welcome!  
Feel free to **fork** this repo and submit a PR.  

---

## 📄 License
Released under the **MIT License** © 2025  

---

<!-- Shields -->
[release-shield]: https://img.shields.io/github/v/release/anthonylucky1909/Photometric-Stereo?style=flat-square
[release-url]: https://github.com/anthonylucky1909/Photometric-Stereo/releases

[build-shield]: https://img.shields.io/github/actions/workflow/status/anthonylucky1909/Photometric-Stereo/ci.yml?branch=master&style=flat-square
[build-url]: https://github.com/anthonylucky1909/Photometric-Stereo/actions

[stars-shield]: https://img.shields.io/github/stars/anthonylucky1909/Photometric-Stereo?style=flat-square
[stars-url]: https://github.com/anthonylucky1909/Photometric-Stereo/stargazers

[license-shield]: https://img.shields.io/github/license/anthonylucky1909/Photometric-Stereo?style=flat-square
[license-url]: https://github.com/anthonylucky1909/Photometric-Stereo/blob/master/LICENSE
