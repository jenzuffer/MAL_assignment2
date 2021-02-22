# MAL assignment 2
## Christian M & Thobias Frehr

## Union-find algorithms implemenation of Quick-union and Weighted-union.

##The chosen language is python3

## UF implementation: 
https://python-algorithms.readthedocs.io/en/stable/_modules/python_algorithms/basic/union_find.html

### The quick-union algorithm is about finding the relation between p and q for example using an indexed array. Important is how the indexed array in quick-union has an entry for each side which will be the name of another side or even itself. following each side and their linked sites until reaching a root. These are tree stuctures where you may combine one large tree with a small tree or a small tree with a large tree.


### The weighted union does not connect the first tree to a second tree like the quick-union does. We keep track of each trees size and that way always ensure to connect the smaller tree to the larger tree. 


### python3 union-find.py

###the UF class is an combination of quick find that involves weighted search

### the UN class is a simpler quick union approach

### meanwhile dict_un_run tries to showcase quick union on dictionaries where it proves that different dictonaries may be part of the same tree or not. 

