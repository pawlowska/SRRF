# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import srrf_cupy.srrf as srrf
import os.path

# read data from a tiff file
file_path=os.path.abspath("X:/FUW/2019_10_07/AF647_63Xoil.tif")
print(os.path.exists(file_path))
img_array = srrf.read_images_from_tiff_file(file_path)    

# run SRRF with default args
ret_img_array = srrf.srrf(img_array)

# show result
srrf.plot_result(img_array, ret_img_array)