from io import StringIO
import csv

'''запустить функцию task,
   передав строку из csv как аргумент'''

def get_data(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    return out

def task(csvString):
    data = get_data(csvString).split('\n')
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
    count_hierarchy = [[] for _ in range(5)]
    for i in tree.keys():
        for j in tree[i]:
            count_hierarchy[0].append(i)# управляет непосредственно
            count_hierarchy[1].append(j) # подчиняется непосредственно
            if len(tree[i]) > 1:
                count_hierarchy[4].append(j) # на одном уровне
            if j in tree:
                count_hierarchy[2].append(i)  # управляет косвенно
                for k in tree[j]:
                    count_hierarchy[3].append(k) # подчиняется косвенно
    for i in range(len(count_hierarchy)):
        count_hierarchy[i] = list(set(count_hierarchy[i]))
    return count_hierarchy
