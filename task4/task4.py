from io import StringIO
import csv
from math import log

'''для расчета энтропии запустить функцию task,
   передав строку из csv как аргумент'''

def get_data(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    return out

def count_final_entropy(num_list, n):
    res = 0
    for i in range(1, len(num_list) - 1):
        res -= num_list[i] * i * log(i/(n - 1), 2) * 1/(n - 1)
    return res

def task(csvString):
    data = get_data(csvString)
    tree = {}
    nodes = set()
    for i in data:
        pair = i.split(',')
        nodes.add(pair[0])
        nodes.add(pair[1])
        if int(pair[0]) not in tree:
            tree[int(pair[0])] = []
        tree[int(pair[0])].append(int(pair[1]))
    n = len(nodes)
    count_hierarchy = [[0]*5 for _ in range(n)]
    for i in tree.keys():
        for j in tree[i]:
            count_hierarchy[i - 1][0] += 1 # управляет непосредственно
            count_hierarchy[j - 1][1] += 1 # подчиняется непосредственно
            count_hierarchy[j - 1][4] += len(tree[i]) - 1 # на одном уровне
            if j in tree:
                count_hierarchy[i - 1][2] += len(tree[j]) # управляет косвенно
                for k in tree[j]:
                    count_hierarchy[k - 1][3] += 1 # подчиняется косвенно
    count_dif_number = [0] * n
    for num_list in count_hierarchy:
        for i in range(1, n):
            count_dif_number[i] += num_list.count(i)
    res = count_final_entropy(count_dif_number, n)
    print(res)
