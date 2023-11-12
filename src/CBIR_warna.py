from PIL import Image
import numpy as np
def open_image_and_preprocess(image_location):
    img = Image.open(image_location) # path
    arr = np.array(img)

    # membagi menjadi blok 4x4 dan rata-rata rgb, untuk gambar png komponen a diabaikan
    NHeight, NWidth = (img.size[1] - (img.size[1] % 4)), (img.size[0] - (img.size[0] % 4))
    arr = arr[:NHeight, :NWidth, :3] # cut jika tidak habis dibagi 4 biar tidak pusing mikirin, cut a jika png
    arr = arr.reshape((NHeight // 4), 4, (NWidth // 4), 4, 3) # compress 4x4
    arr = arr.mean(axis = (1, 3))

    # ubah dari rgb ke hsv (fungsi rgb_to_hsv dibikin sendiri (salin rumus dari spesifikasi) RIL NO FEK NO FEK)
    for i in range (len(arr)):
        for j in range (len(arr[0])):
            arr[i][j][0], arr[i][j][1], arr[i][j][2] = rgb_to_hsv(arr[i][j][0], arr[i][j][1], arr[i][j][2])
    return arr # arr[height][width] = [h, s, v], float

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