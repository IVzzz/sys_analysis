import json
import numpy as np


def get_data_matrix(data_str):
    try:
        return json.loads(data_str)
    except json.decoder.JSONDecodeError:
        data = data_str.split('\n')
        data = [i.split(',') for i in data]
        return data


def get_float_matrix(data):
    for i in range(len(data)):
        if type(data[i]) == list:
            for j in range(len(data[i])):
                data[i][j] = float(data[i][j])
        elif type(data[i]) == str:
            data[i] = [float(data[i])]


def get_pairwise_comparisons_matrix(obj_scores):
    n = len(obj_scores)
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            if obj_scores[i] < obj_scores[j]:
                matrix[i].append(1)
            elif obj_scores[i] == obj_scores[j]:
                matrix[i].append(0.5)
            else:
                matrix[i].append(0)
    return matrix


def get_probability_matrix(pairwise_matrix, count_experts, count_objects):
    return np.sum(pairwise_matrix, axis=0) / count_experts


def get_distance(v1, v2):
    return max([abs(v1[i] - v2[i]) for i in range(len(v1))])


def task(data_str):
    rang = get_data_matrix(data_str)

    get_float_matrix(rang)
    count_experts = len(rang)
    count_objects = len(rang[0])

    pairwise_matrix = [get_pairwise_comparisons_matrix(obj_scores) for obj_scores in rang]

    X = get_probability_matrix(pairwise_matrix, count_experts, count_objects)
    E = 0.001
    v = [1]*count_objects
    K_prev = [0] * count_objects
    K = np.array([1/count_objects for _ in range(count_objects)])
    while get_distance(K, K_prev) > E:
        Y = np.dot(X,K.T)
        lmd = np.array(np.dot(v, Y))
        K_prev = K
        K = Y / lmd
    K = [round(i, 3) for i in K]
    return K