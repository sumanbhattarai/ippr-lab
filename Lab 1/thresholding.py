import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv2.imread('sumanbhattarai.jpeg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Threshold = 120
# All pixels value above threshold will be set to 255
ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)


#Display
cv2.imshow('Binary Threshold', thresh)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
