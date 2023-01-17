from PIL import Image
import numpy as np


def bw_convert():
    img = Image.open("image.jpg")
    arr = np.asarray(img)
    c = np.array((0.2989, 0.5870, 0.1140))
    res = np.round(np.sum(arr * c, axis=2))
    Image.fromarray(res).convert("RGB").save("image_res.jpg")


bw_convert()
