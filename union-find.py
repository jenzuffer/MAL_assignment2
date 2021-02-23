from uf import UF
from un import UN
from weighteduf import WUF

def uf_call(number_of_items, edges):
    uf = UF(number_of_items)
    for p, q in edges:
        uf.union(p, q) #encapsulation
    print_method(('uf ids: ', uf))

def un_call(number_of_items, edges):
    un = UN(number_of_items)
    for p, q in edges:
        un.union(p, q)
    print_method(('un: ', un))

def print_method(msg):
    print(msg, flush=True)

def uf_run(edges_example):
    print_method(('running :', edges_example))
    uf_call(len(edges_example), edges_example)

def un_run(edges_example):
    print_method(('running :', edges_example))
    un_call(edges_example, edges_example)



def dict_generate_tree_double_nodes(size):
    scope_dict = {"char_value": chr(0)}
    scope_dict["number"] = 0
    scope_dict["id"] = scope_dict #root node
    scope_list = [scope_dict]
    counter = 0
    for index in range(1, size):
        local_dict = {"char_value": chr(index)}
        local_dict["number"] = index
        local_dict["id"] = scope_dict #appending node to parent node
        print_method(('iterating index: ', index, 'local_dict: ', local_dict))
        counter += 1
        scope_list.append(local_dict)
        if counter % 2 == 0:
            node_index = scope_dict["number"]
            scope_dict = scope_list[node_index + 1] #switching parent node to next
    return scope_list
        
def are_nodes_connected(scope_list):
    for index in range(1, len(scope_list)):
       print_method((dict_connected(scope_list[index - 1], scope_list[index])))

def wuf_run(edges):
    weighted_union = WUF(len(edges))
    for p, q in edges:
        weighted_union.union(p, q)
    print_method(('weighted union: ', weighted_union))

def dict_un_run():
    a = {"name":"a"}
    b = {"name":"b"}
    c = {"name":"c"}
    d = {"name":"d"}
    e = {"name":"e"}
    f = {"name":"f"}
    a["id"] = a # it is a root of a tree
    b["id"] = a # same group as a
    c["id"] = c # root of different tree
    d["id"] = c # same group as c
    e["id"] = c # same group as c
    f["id"] = d # same group as c, but child of d 
    result = dict_connected(e, f)
    print_method(result)
    result = dict_connected(b, d)
    print_method(result)
    result = dict_connected(c, f)
    print_method(result)

def dict_connected(node1, node2):
    print_method(('node1: ', node1))
    print_method(('node2: ', node2))
    while node1["id"] != node1:
        #print_method(('node1: ', node1))
        node1 = node1["id"]
    while node2["id"] != node2:
        #print_method(('node2: ', node2))
        node2 = node2["id"]
    return node1 == node2

def main():
    uf_run([(1, 4), (4, 2), (2, 3), (3, 3), (2, 1), (3, 4)])
    uf_run([(6, 4), (8, 2), (2, 5), (7, 3), (7, 1), (10, 8), (6, 2), (5, 4), (1, 5), (4, 6), (9, 5), (10, 4)])
    print_method('now running simpler union method')
    un_run([(1, 4), (4, 2), (2, 3), (3, 3), (2, 1), (3, 4)])
    un_run([(6, 4), (8, 2), (2, 5), (7, 3), (7, 1), (10, 8), (6, 2), (5, 4), (1, 5), (4, 6), (9, 5), (10, 4)])
    print_method('now running dict quick-union implementation')
    dict_un_run()
    scope_list = dict_generate_tree_double_nodes(10)
    are_nodes_connected(scope_list)
    scope_list = dict_generate_tree_double_nodes(30)
    are_nodes_connected(scope_list)
    print_method(('now attempting weighted union'))
    wuf_run([(1, 4), (4, 2), (2, 3), (3, 3), (2, 1), (3, 4)])
    wuf_run([(6, 4), (8, 2), (2, 5), (7, 3), (7, 1), (10, 8), (6, 2), (5, 4), (1, 5), (4, 6), (9, 5), (10, 4)])

if __name__ == '__main__':
    main()
