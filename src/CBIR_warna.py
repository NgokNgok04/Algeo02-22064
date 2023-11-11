from PIL import Image
def open_image(image_location):
    img = Image.open(image_location) # path
    width, height = img.size[0], img.size[1]
    NewW, NewH = width // 4, height // 4
    f = len(img.getpixel((0, 0))) # 3 - jpg, 4 - png
    arr = [[[0 for _ in range (3)] for _ in range (NewH)] for _ in range (NewW)] # apakah ada cara lebih bagus
    # sudah sekaligus dibagi jadi blok 4x4
    # kalau tidak habis dibagi 4 terpotong
    if (f == 3):
        for i in range (width):
            for j in range (height):
                for k in range (3):
                    arr[i // 4][j // 4][k] += img.getpixel((i, j))[k]
    else:
        for i in range (width):
            for j in range (height):
                for k in range (3):
                    arr[i // 4][j // 4][k] += (img.getpixel((i, j))[k]) * ((img.getpixel((i, j))[3]) / 255)
    for i in range(NewW):
        for j in range (NewH):
            for k in range (3):
                arr[i][j][k] = arr[i][j][k] / 16
            
            # convert to hsv sekalian
            arr[i][j][0], arr[i][j][1], arr[i][j][2] = rgb_to_hsv(arr[i][j][0], arr[i][j][1], arr[i][j][2])
    return arr # arr[width][height] = [h, s, v]

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