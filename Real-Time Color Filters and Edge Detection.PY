import cv2
import numpy as np

def apply_filter(image, ftype):
    """Apply a filter to the image based on the filter type"""
    img = image.copy()
    if ftype == "red tint":
        img[:, :, 1] = img[:, :, 0] = 0 
    elif ftype == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0
    elif ftype == "blue_tint":
        img[:, :, 1] = img[:, :, 2] = 0
    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)