import numpy as np
from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from lpr_image import gray_car_image, binary_car_image

#get label image
label_image = measure.label(binary_car_image)

#apply vertical projection on the binary car image
vertical_proj = np.sum(binary_car_image, axis =0)
projection_thresh = 0.1*np.max(vertical_proj)
sig_cols = vertical_proj<projection_thresh

#Use the ratio and the usual size of the license plate to eliminate other redundant bounding box from labelling
plate_dimensions = (0.04*label_image.shape[0], 0.1*label_image.shape[0], 0.08*label_image.shape[1], 0.4*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimensions

#creating two lists to store plate like objects and their coordinates
plate_objects_cordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(gray_car_image,cmap="gray")


for region in regionprops(label_image):
    if region.area<50:
        continue #ignore regions that are too small

    minRow, minCol, maxRow, maxCol = region.bbox
    region_height = maxRow- minRow
    region_width =  maxCol-minCol

    #nested if statements to further filter out non-license plate areas
    if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height: #potentially simply this

        plate_region = binary_car_image[minRow:maxRow, minCol:maxCol]
        region_vProjection  = np.sum(plate_region, axis =0)
        sig_columns = np.sum(region_vProjection<projection_thresh)

        if sig_columns>region_width*0.5:
            extent = region.extent
            solidity = region.solidity
            if solidity < 0.1 or extent > 0.55:
                plate_like_objects.append(binary_car_image[minRow:maxRow, minCol:maxCol])
                plate_objects_cordinates.append((minRow, minCol, maxRow, maxCol))
                recBorder = patches.Rectangle((minCol, minRow), maxCol - minCol, maxRow - minRow, edgecolor="red",
                                              linewidth=2, fill=False)
                ax1.add_patch(recBorder)





