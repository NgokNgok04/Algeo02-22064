import os
from PIL import Image
import numpy as np
import math

def gscale_to_co_occur(matrix, mat_cooccur):
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width-1):
            mat_cooccur[matrix[i][j]][matrix[i][j+1]] += 1

def transpose_matrix(matrix, mat_transpose):
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width):
            mat_transpose[j][i] = matrix[i][j]

def sym_matrix(matrix, mat_transpose):
    mat_sym = [[0 for i in range(256)] for j in range(256)]
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width):
            mat_sym[i][j] = matrix[i][j] + mat_transpose[i][j]
    return mat_sym

def normalized_matrix(matrix, mat_norm):
    sum = 0
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width):
            sum += matrix[i][j]
    for i in range(height):
        for j in range(width):
            mat_norm[i][j] = matrix[i][j]/sum

def contrast(matrix):
    result = 0
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width):
            result += matrix[i][j]*(pow(i-j,2))
    return result

def homogeneity(matrix):
    result = 0
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width):
            result += (matrix[i][j])/(1 + pow(i-j,2))
    return result

def entropy(matrix):
    result = 0
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width):
            if (matrix[i][j] != 0):
                result += matrix[i][j]*math.log10(matrix[i][j])
    result = -result
    return result

def rgb_to_gscale(R,G,B):
    Y = 0.299*R + 0.587*G + 0.114*B
    Y = round(Y)
    return Y

def cbir_texture(image_path):
    img_cooccur = [[0 for i in range(256)] for j in range(256)]
    transpose_coocur = [[0 for i in range(256)] for j in range(256)]
    norm_matrix = [[0 for i in range(256)] for j in range(256)]
    vektor = []
    img = Image.open(image_path)
    img_grayscale = []
    width, height = img.size
    for i in range(height):
        gscale = []
        for j in range(width):
            r, g, b = img.getpixel((i, j))
            grayscale = rgb_to_gscale(r,g,b)
            gscale.append(grayscale)
        img_grayscale.append(gscale)
    gscale_to_co_occur(img_grayscale, img_cooccur)
    transpose_matrix(img_cooccur, transpose_coocur)
    normalized_matrix(sym_matrix(img_cooccur, transpose_coocur), norm_matrix)
    Contrast = contrast(norm_matrix)
    homogein = homogeneity(norm_matrix)
    Entropy = entropy(norm_matrix)
    vektor.append(Contrast)
    vektor.append(homogein)
    vektor.append(Entropy)
    return vektor

def cbir_dataset(folder_path):
    list_files = os.listdir(folder_path)
    dataset_vektor = []
    for f in list_files :
        print(f)
        image_path = os.path.join(folder_path, f)
        dataset_vektor(cbir_texture(image_path))
    return dataset_vektor



def similarity(vektora,vektorb):
    pembilang = 0
    lena = 0
    lenb = 0
    for i in range(len(vektora)):
        pembilang += vektora[i]*vektorb[i]
        lena += pow(vektora[i],2)
        lenb += pow(vektorb[i],2)
    penyebut = math.sqrt(lena)*math.sqrt(lenb)
    similar = pembilang/penyebut
    return similar
