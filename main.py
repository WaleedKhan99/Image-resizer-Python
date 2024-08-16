# cv2 is openCV python library, but not built in library.
import cv2

# Configuration Parameters
source = "Waleed Ahmed Khan.jpg"
destinatoion = "New-Image.png"
title = "Waleed"
#percent by which the image is resized 
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow(title, src)

#calculate the 50 percent of original dimensions
# src.shape is a numpy element and in this 1 is use for width and 0 for height

new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destinatoion, output)
cv2.waitKey(0)


