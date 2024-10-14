import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt


# desired_size = (1080,1920)

car_image = imread("/Users/steventhesteve/license-plate-recognition/car4.jpg", as_gray=True)
car_image = np.squeeze(car_image)

# resized_car_image = resize(car_image, desired_size)
print(car_image.shape)

gray_car_image = car_image*255
fig, (ax1,ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image, cmap = "gray")

threshold_value = threshold_otsu(gray_car_image)
binary_car_image = gray_car_image>threshold_value
ax2.imshow(binary_car_image, cmap = "gray")
# plt.show()

