## Digital Image Processing — Lab 3

Edge detection and image transformation experiments using **Python, OpenCV, NumPy, and Matplotlib**.

## 📁 Folder Structure

```text
task-3/
├── edge_detection_by_derivative.py
├── robert_edge_detection.py
├── sobel_edge_detection.py
├── wavelet_transform.py
├── README.md
└── images/
    ├── edge.png
    ├── prewitt_edge.png
    ├── prewitt_gx.png
    ├── prewitt_gy.png
    ├── roberts_edge.png
    ├── roberts_threshold.png
    ├── sobel_edge.png
    ├── sobel_gx.png
    ├── sobel_gy.png
    ├── threshold_edge.png
    ├── x_edge.png
    ├── y_edge.png
    └── wavelet_transform.jpg
```

**📂 Experiments**

**1. Edge Detection by Derivative**

Detecting image edges by calculating first-order spatial derivatives along horizontal and vertical directions, followed by gradient magnitude computation and thresholding.

<p align="center">
  <img src="images/x_edge.png" width="220">
  <img src="images/y_edge.png" width="220">
  <img src="images/edge.png" width="220">
  <img src="images/threshold_edge.png" width="220">
</p>

<p align="center">
  <b>X Direction Edge</b>&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Y Direction Edge</b>&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Overall Edge</b>&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Threshold Edge</b>
</p>

**2. Sobel Edge Detection**

Applying 3×3 Sobel convolution kernels to extract horizontal ($G_x$) and vertical ($G_y$) gradients and compute the gradient magnitude edge map.

<p align="center">
  <img src="images/sobel_gx.png" width="260">
  <img src="images/sobel_gy.png" width="260">
  <img src="images/sobel_edge.png" width="260">
</p>

<p align="center">
  <b>Sobel Gx</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Sobel Gy</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Sobel Edge</b>
</p>

**3. Prewitt Edge Detection**

Utilizing 3×3 Prewitt operators to identify horizontal and vertical gradient components and combined edge boundaries.

<p align="center">
  <img src="images/prewitt_gx.png" width="260">
  <img src="images/prewitt_gy.png" width="260">
  <img src="images/prewitt_edge.png" width="260">
</p>

<p align="center">
  <b>Prewitt Gx</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Prewitt Gy</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Prewitt Edge</b>
</p>

**4. Roberts Cross Edge Detection**

Applying diagonal 2×2 Roberts Cross difference operators to highlight sharp edge transitions and thresholding the output.

<p align="center">
  <img src="images/roberts_edge.png" width="350">
  <img src="images/roberts_threshold.png" width="350">
</p>

<p align="center">
  <b>Roberts Edge</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <b>Roberts Thresholded Edge</b>
</p>

**5. Discrete Wavelet Transform (DWT)**

Decomposing the image using 2D Haar Wavelet Transform into approximation (LL), horizontal detail (LH), vertical detail (HL), and diagonal detail (HH) sub-bands.

<p align="center">
  <img src="images/wavelet_transform.jpg" width="450">
</p>

<p align="center">
  <b>2D Wavelet Decomposition (LL, LH, HL, HH)</b>
</p>
