import time

def readGraph(dirname):
    
    graph = []
    with open(dirname, 'r') as f:
        num_of_node = f.readline()
        for line in f.readlines():
            a = line.strip('[]\n')
            a = a.split(',')
            item_graph = [int(x) for x in a]
            if item_graph[0] == -1:
                item_graph = []
            graph.append(item_graph)
    return graph, int(num_of_node)


def find_all_length_path(graph, length, pre_path):
    pre_path = pre_path
    # pre_path = find_all_length_path(graph, length-1)
    all_path = []
    for prepath in pre_path:
        if len(prepath) > 1 and prepath[0] == prepath[-1]: # 如果末尾的node等于路径的开始node
            continue
        
        for next_node in graph[prepath[-1]]:
            if next_node in prepath[1:]: 
                continue
            node = prepath.copy()
            node.append(next_node)
            all_path.append(node)
    
    return all_path

def prime_path(simple_path_list):
    # simple_path_list = sorted(simple_path_list, key=lambda simple_path_list: len(simple_path_list))
    prime_path_list = []

    length = len(simple_path_list)

    for i in range(length):
        flag = True
        # path = ','.join(simple_path_list[i])
        # str_i = ','.join([str(x) for x in simple_path_list[i]])
        for j in range(length-1, i, -1):
            if simple_path_list[i] in simple_path_list[j]:
                flag = False
                break
        
        if flag:
            prime_path_list.append(simple_path_list[i])

    return prime_path_list



if __name__ == "__main__":
    start = time.time()
    dirname = '.\\softwareTest\\test.txt'
    graph, numOfNode = readGraph(dirname)
    # numOfNode = len(graph)
    # all_path = []
    pre_path = []
    
    all_path = [[x] for x in range(numOfNode)]
    for i in range(1, numOfNode+1):
        pre_path = [x for x in all_path if len(x) == i-1]
        all_path.extend(find_all_length_path(graph, i, pre_path))
    all_path_str = []
    for i in range(len(all_path)):
        path_str = ','.join([str(x) for x in all_path[i]])
        path_str += ','
        all_path_str.append(path_str)
    prime_path_list = prime_path(all_path_str)
    end = time.time()
    print('num of all path:', len(all_path_str),' time:%.6f' % (end-start))
    print('num of prime path:', len(prime_path_list), ' time:%.6f' % (end-start))
