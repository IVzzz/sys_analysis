import json
import numpy as np


def get_int_matrix(data):
    for i in range(len(data)):
        if type(data[i]) == list:
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])
        elif type(data[i]) == str:
            data[i] = [int(data[i])]


def get_size_matrix(data):
    res = 0
    for i in data:
        res += len(i)
    return res


def find_group_index(data, num):
    for i in range(len(data)):
        if num in data[i]:
            return i
    return -1


def create_table(rang):
    matrix = []
    dim = get_size_matrix(rang)
    for i in range(dim):
        l = [0] * dim
        for j in range(find_group_index(rang, i + 1), -1, -1):
            for elem in rang[j]:
                l[elem - 1] = 1
        matrix.append(l)
    return np.matrix(matrix)


def get_kernel(table):
    kern = []
    for i in range(table.shape[0]):
        for j in range(i, table.shape[1]):
            if table[i, j] == 0:
                kern.append([str(i + 1),str(j + 1)])
    return kern


def task(json1, json2):
    rang1 = json.loads(json1)
    rang2 = json.loads(json2)
    get_int_matrix(rang1)
    get_int_matrix(rang2)

    res_table = np.multiply(create_table(rang1), create_table(rang2)).T
    kern = get_kernel(res_table)

    return kern
