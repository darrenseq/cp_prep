# Star Sum - Zscalar interview

# test 1 
# g_from = [3,3,3,3]
# g_to = [1, 2, 4, 5]
# values = [10,20,30,40,50]
# k = 2

# test 2
g_from =    [0, 1,  1,  3,  3,  3]
g_to =      [1, 2,  3,  4,  5,  6]
values =    [1, 2,  3,  4,  10, -10, -20]
k = 2

def add_node(g_from, g_to):
    return set(g_from + g_to)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    return adj

def prGraph(adj, node_length):
    result = {}
    for node in range(node_length):
        if len(adj[node]) > k:   
            result[node] = []
            # print("vertex " + str(v), end = ' ')
            for x in adj[node]:
                # print("-> " + str(x), end = '')
                result[node].append(x)
            # print()
    # print()
    return result

def graph_values(adj_list, values_dict):
    result = []
    for node, relation_nodes in adj_list.items():
        relation_values = []
        relation_values.append(values_dict[node])
        
        for x in relation_nodes:
            relation_values.append(values_dict[x])
        result.append(relation_values)   

    return result

def bestSumKStar(g_from, g_to, values, k):
    #Adding nodes
    nodes = add_node(g_to, g_from)

    # Add Node weights
    values_dict = dict(zip(nodes, values))

    # Create adjacency list 
    adj_list = [[] for i in range(len(nodes))]
    for i in range(len(g_from)):
        add_edge(adj_list, g_from[i], g_to[i])
    
    # Filter nodes with only minimum K relations
    adj_list = prGraph(adj_list, len(nodes))

    # Replace nodes by their values
    relation_values = graph_values(adj_list, values_dict)
    
    # Sort each relation node in descending order 
    sorted_sums = []
    for x in relation_values:
        sorted_sums.append(sorted(x, reverse = True))

    # Get the k+1 sum combinations from each relation
    max_list = []
    for x in sorted_sums:
        max_list.append(sum(x[:k+1]))

    # return max sum
    return max(max_list)

# Driver
print(bestSumKStar(g_from, g_to, values, k)) 