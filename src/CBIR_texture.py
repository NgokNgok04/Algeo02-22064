import os
from PIL import Image
import numpy as np
import math
import multiprocessing
import json

def gscale_to_co_occur(matrix, mat_cooccur):
    matrix = np.array(matrix)
    height,width = matrix.shape
    for i in range(height):
        for j in range(width-1):
            mat_cooccur[matrix[i][j]][matrix[i][j+1]] += 1

def sym_matrix(matrix):
    matrix = np.array(matrix)
    return matrix + matrix.T

def normalized_matrix(matrix, mat_norm):
    matrix = np.array(matrix)
    total_sum = matrix.sum()
    mat_norm[:] = matrix / total_sum

def contrast(matrix):
    matrix = np.array(matrix)
    i, j = np.indices(matrix.shape)
    return np.sum(matrix * (pow(i-j,2)))

def homogeneity(matrix):
    matrix = np.array(matrix)
    i, j = np.indices(matrix.shape)
    return np.sum(matrix / (1 + (pow(i-j,2))))

def entropy(matrix):
    matrix = np.array(matrix)
    not_zero_elmts = matrix[matrix != 0]
    return -np.sum(not_zero_elmts * np.log10(not_zero_elmts))

def rgb_to_gscale(R,G,B):
    return round(0.299 * R + 0.587 * G + 0.114 * B)
    
def cbir_texture(image_path):
    img_cooccur = [[0 for i in range(256)] for j in range(256)]
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
    normalized_matrix(sym_matrix(img_cooccur), norm_matrix)
    Contrast = contrast(norm_matrix)
    homogein = homogeneity(norm_matrix)
    Entropy = entropy(norm_matrix)
    vektor.append(Contrast)
    vektor.append(homogein)
    vektor.append(Entropy)
    vektor_and_path = {"image_path": image_path, "vektor": vektor}
    return vektor_and_path

def cbir_dataset(folder_path):
    list_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
    with multiprocessing.Pool() as pool:
        dataset_vektor = pool.map(cbir_texture, list_files)
    return dataset_vektor

def dataset_to_json(vektor_dataset):
    with open("dataset_vektor.json", 'w') as json_file:
        json.dump(vektor_dataset, json_file, indent=4)

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

def read_from_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def similarity_sorting(dataset_array):
    sorted_people = sorted(dataset_array, key=lambda x: x['similarity_score'], reverse=True)
    return sorted_people

def compare_and_write_results(image_path, dataset_vectors_path):
    with open(dataset_vectors_path) as file:
        jsonArray = json.load(file)
    image_vector = cbir_texture(image_path)
    results = []
    for current_object in jsonArray:
        similarity_score = similarity(image_vector['vektor'], current_object['vektor'])
        if similarity_score>0.60:
            results.append({"image_path": current_object['image_path'], "similarity_score": similarity_score})
    results = similarity_sorting(results)
    with open("compare_result.json", 'w') as output_json_file:
        json.dump(results, output_json_file, indent=4)

if __name__ == "__main__":
    target_folder = "testing2"
    dataset_to_json(cbir_dataset(target_folder))
    image_path = "testing//0.jpg"
    compare_and_write_results(image_path, "dataset_vektor.json")