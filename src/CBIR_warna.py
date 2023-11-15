from PIL import Image
import numpy as np
import os
import json
import time
def open_folder(folder_location):
    Image_List = np.array(os.listdir(folder_location))
    Image_List = np.core.defchararray.add(folder_location, Image_List)
    return Image_List

def open_image_to_Vector(image_location):
    img = Image.open(image_location) # path
    arr = np.array(img)

    # compress
    arr = compress(arr)

    # ubah dari rgb ke histogram hsv
    arr = rgb_to_hsv_histBinArray(arr)
    bins = [i for i in range (73)]
    arr, _ = np.histogram(arr, bins = bins)

    # arr array 1D dengan panjang 72, tinggal dipakai untuk cosine similarity
    return arr

def compress(Image_Array):
    # membagi menjadi blok 4x4 dan rata-rata rgb, untuk gambar png komponen a diabaikan
    NHeight, NWidth = ((len(Image_Array)) - ((len(Image_Array)) % 4)), ((len(Image_Array[0])) - ((len(Image_Array[0])) % 4))
    Image_Array = Image_Array[:NHeight, :NWidth, :3] # cut jika tidak habis dibagi 4 biar tidak pusing mikirin, cut a jika png
    NHeight, NWidth = (NHeight // 4), (NWidth // 4)
    Image_Array = Image_Array.reshape(NHeight, 4, NWidth, 4, 3) # compress 4x4
    Image_Array = Image_Array.mean(axis = (1, 3))
    return Image_Array

def rgb_to_hsv(r, g, b):
    # ubah dari rgb ke hsv (fungsi rgb_to_hsv dibikin sendiri (salin rumus dari spesifikasi) RIL NO FEK NO FEK)
    Cmax, Cmin = max(r, g, b), min(r, g, b)
    d = Cmax - Cmin
    if (d == 0): H = 0
    elif (Cmax == r): H = 60 * (((g - b) / d) % 6)
    elif (Cmax == g): H = 60 * (((b - r) / d) + 2)
    else: H = 60 * (((r - g) / d) + 4)
    if (Cmax == 0): S = 0
    else: S = d / Cmax
    return H, S, Cmax

def hsv_to_histidx(h, s, v):
    # h dibagi 8, s dibagi 3, v dibagi 3
    if ((h == 0) or (h > 315)): H = 0
    elif (h <= 25): H = 1
    elif (h <= 40): H = 2
    elif (h <= 120): H = 3
    elif (h <= 190): H = 4
    elif (h <= 270): H = 5
    elif (h <= 295): H = 6
    else: H = 7

    if (s < 0.2): S = 0
    elif (s < 0.7): S = 1
    else: S = 2

    if (v < 0.2): V = 0
    elif (v < 0.7): V = 1
    else: V = 2

    idx = (H * 9) + (S * 3) + V # idx 0 - 71
    return idx

def rgb_to_hsv_histBinArray(array):
    array = array.reshape(-1, 3)
    array = array / 255
    array = [tuple(x) for x in array]

    # mengubah jadi array of tuple HSV
    array = np.array([rgb_to_hsv(R, G, B) for R, G, B in array], dtype = [('x', float), ('y', float), ('z', float)])

    array = np.array([hsv_to_histidx(h, s, v) for h, s, v in array])

    return array

def cosine_similarity(Vector1, Vector2):
    dot_product = np.sum(np.multiply(Vector1, Vector2))
    Vector1_Length = np.sqrt(np.sum(np.square(Vector1)))
    Vector2_Length = np.sqrt(np.sum(np.square(Vector2)))
    similarity = dot_product / (Vector1_Length * Vector2_Length)
    return similarity

def similarity_list(Image_Input, Image_Dataset):
    # Image_Input adalah string yang berisi path ke gambar masukan
    # Image_Dataset adalah list (np.array) yang berisi string semua path ke semua gambar dataset
    Vector_Input = open_image_to_Vector(Image_Input)
    Cos_Sim_List = [0 for _ in range (len(Image_Dataset))]
    for i in range (len(Cos_Sim_List)):
        Vector_Compare = open_image_to_Vector(Image_Dataset[i])
        Cos_Sim_List[i] = cosine_similarity(Vector_Input, Vector_Compare)
    Cos_Sim_List = list(zip(Image_Dataset, Cos_Sim_List))
    Cos_Sim_List = sorted(Cos_Sim_List, key = lambda x: x[1], reverse = True)
    return Cos_Sim_List

def write_JSON(SimList, outputFile_Path):
    with open(outputFile_Path, 'w') as file:
        for i in range (len(SimList)):
            data = {
                "path": SimList[i][0],
                "Sim": SimList[i][1]
            }
            json.dump(data, file, indent = 0)
    return
"""
test
start = time.time()
Input = "../test/0.jpg"
Dataset = open_folder("../test/")
sim = similarity_list(Input, Dataset)
write_JSON(sim, "output.json")
print(time.time() - start)
"""

#python3 CBIR_warna.py