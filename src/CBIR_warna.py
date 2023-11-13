from PIL import Image
import numpy as np
def open_image_and_preprocess(image_location):
    img = Image.open(image_location) # path
    arr = np.array(img)

    # compress
    arr = compress(arr)

    # ubah dari rgb ke histogram hsv
    arr = rgb_to_hsv_histBinArray(arr)
    bins = [i for i in range (65)]
    arr, _ = np.histogram(arr, bins = bins)

    # arr array 1D dengan panjang 64, tinggal dipakai untuk cosine similarity
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
    # ubah dari rgb ke hsv (fungsi rgb_to_hsv dibikin sendiri (salin rumus dari spesifikasi) RIL NO FEK NO FEK)
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

def rgb_to_hsv_histBinArray(rgb_array):
    Height, Width = len(rgb_array), len(rgb_array[0])
    r, g, b = rgb_array[..., 0], rgb_array[..., 1], rgb_array[..., 2] # r, g, b itu array 2D yang isinya r, g, b dari gambar
    r, g, b = r.reshape(Height * Width), g.reshape(Height * Width), b.reshape(Height * Width) # jadi array 1D

    # mengubah jadi array of tuple HSV
    hsv = np.array([rgb_to_hsv(R, G, B) for R, G, B in zip(r, g, b)], dtype = [('x', float), ('y', float), ('z', float)])

    hist_idx = np.array([hsv_to_histidx(h, s, v) for h, s, v in hsv])

    return hist_idx

def cosine_similarity(Vector1, Vector2):
    dot_product, Vector1_Length, Vector2_Length = 0, 0, 0
    for i in range (64):
        dot_product += Vector1[i] * Vector2[i]
        Vector1_Length += Vector1[i] * Vector1[i]
        Vector2_Length += Vector2[i] * Vector2[i]
    Vector1_Length, Vector2_Length = (Vector1_Length ** 0.5), (Vector2_Length ** 0.5)
    similarity = dot_product / (Vector1_Length * Vector2_Length)
    return similarity
