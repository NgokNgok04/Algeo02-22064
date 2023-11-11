from PIL import Image
def open_image(image_location):
    img = Image.open(image_location) # path
    width = img.size[0]
    height = img.size[1]
    f = len(img.getpixel((0, 0))) # 3 - jpg, 4 - png
    arr = [[[0 for _ in range (f)] for _ in range (height)] for _ in range (width)] # apakah ada cara lebih cepattt
    for i in range (width):
        for j in range (height):
            for k in range (f):
                arr[i][j][k] = img.getpixel((i, j))[k]
    return arr # arr[width][height] = [r, g, b, a(kalau png)]

def rgb_to_hsv(r, g, b):
    R, G, B = r / 255, g / 255, b / 255
    Cmax, Cmin = max(R, G, B), min(R, G, B)
    d = Cmax - Cmin
    if (d == 0): H = 0
    elif (Cmax == R): H = 60 * (((G - B) / d) % 6)
    elif (Cmax == G): H = 60 * (((B - R) / d) + 2)
    else: H = 60 * (((R - G) / d) + 4)
    if (Cmax == 0): S = 0
    else: S = d / Cmax
    return H, S, Cmax