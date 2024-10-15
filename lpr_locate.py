import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import lpr_findConnected


license_plate = np.invert(lpr_findConnected.plate_like_objects[0])
labelled_plate = measure.label(license_plate)
fig, (ax1) = plt.subplots(1)
ax1.imshow(license_plate, cmap = "gray")


#specify character dimension to accurately extract the characters
character_dimensions = (0.45*license_plate.shape[0], 0.8*license_plate.shape[0], 0.05*license_plate.shape[1],0.2*license_plate.shape[1])
min1_height, max1_height, min1_width, max1_width = character_dimensions

characters = []
coutner = 0
column_list = []
for regions in regionprops(labelled_plate):
    y0, x0, y1, x1 = regions.bbox
    region1_height = y1-y0
    region1_width = x1-x0
    if region1_height>min1_height and region1_height<max1_height and region1_width>min1_width and region1_width<max1_width:
        roi = license_plate[y0:y1, x0:x1]

        rec_border = patches.Rectangle((x0, y0), x1-x0, y1-y0, edgecolor="red", linewidth=2, fill= False)
        ax1.add_patch(rec_border)
        resized_char  = resize(roi, (20,20))
        characters.append(resized_char)
        column_list.append(x0)

# plt.show()
