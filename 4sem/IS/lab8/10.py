with open("bmp_image.bmp", "rb") as bmp_image:
    data = list(bytes(bmp_image.read()))

data_negative = []
for count, byte in enumerate(data):
    if count < 54:
        data_negative.append(byte)
    else:
        data_negative.append(255 - byte)

with open("bmp_image_res.bmp", "wb") as bmp_image:
    bmp_image.write(bytes(data_negative))
