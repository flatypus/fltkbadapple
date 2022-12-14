import numpy as np
import cv2
import skimage.exposure
import pickle
from PIL import Image

# read mp4 file
vidcap = cv2.VideoCapture('badapple.mp4')
success, image = vidcap.read()

count = 0
all_frames = []
while success:
    success, image = vidcap.read()
    if (count % 3 == 0):
        blur = cv2.GaussianBlur(image, (0, 0), sigmaX=3,
                                sigmaY=3, borderType=cv2.BORDER_DEFAULT)
        result = skimage.exposure.rescale_intensity(
            blur, in_range=(127.5, 255), out_range=(0, 255))
        grayscale = cv2.cvtColor(result.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        shrunk = cv2.resize(grayscale, (72, 56))
        ret, binary = cv2.threshold(shrunk, 127, 1, cv2.THRESH_BINARY)
        # Image.fromarray(shrunk).save(f"binary/{count}.png")
        binary = [i.tolist() for i in binary]
        all_frames.append(binary)
        # print(binary)
        print("Frame", count)
    count += 1


pickle.dump(all_frames, open("binary.pickle", "wb"))
