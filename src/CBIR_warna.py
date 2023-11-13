from PIL import Image
import numpy as np
def open_image_and_preprocess(image_location):
    img = Image.open(image_location) # path
    arr = np.array(img)

    # compress
    arr = compress(arr)

    # ubah dari rgb ke hsv (fungsi rgb_to_hsv dibikin sendiri (salin rumus dari spesifikasi) RIL NO FEK NO FEK)
    Height, Width = len(arr), len(arr[0])
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    r, g, b = r.reshape(Height * Width), g.reshape(Height * Width), b.reshape(Height * Width)
    hsv = [rgb_to_hsv(R, G, B) for R, G, B in zip(r, g, b)]
    h, s, v = map(np.array, zip(*hsv))
    h, s, v = h.reshape(Height, Width), s.reshape(Height, Width), v.reshape(Height, Width)
    arr = np.stack([h, s, v], axis=-1)

    return arr

def compress(Image_Array):
    # membagi menjadi blok 4x4 dan rata-rata rgb, untuk gambar png komponen a diabaikan
    NHeight, NWidth = ((len(Image_Array)) - ((len(Image_Array)) % 4)), ((len(Image_Array[0])) - ((len(Image_Array[0])) % 4))
    Compressed_Image_Array = Image_Array[:NHeight, :NWidth, :3] # cut jika tidak habis dibagi 4 biar tidak pusing mikirin, cut a jika png
    NHeight, NWidth = (NHeight // 4), (NWidth // 4)
    Compressed_Image_Array = Compressed_Image_Array.reshape(NHeight, 4, NWidth, 4, 3) # compress 4x4
    Compressed_Image_Array = Compressed_Image_Array.mean(axis = (1, 3))
    return Compressed_Image_Array

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

def hsv_to_histidx(h, s, v):
    # h dibagi 8, s dibagi 2, v dibagi 4
    H = ((h + 22.5) % 360) // 45
    S = s // 0.5
    if (S == 2): S = 1 # kalau s == 1
    V = v // 0.25
    if (V == 4): V = 3 # kalau v == 1
    idx = (H * 8) + (S * 4) + V # idx 0 - 63
    return idx

arr = open_image_and_preprocess("../test/Jadwal_Clan_Training_3.png")
# python3 CBIR_warna.py