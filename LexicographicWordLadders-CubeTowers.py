#import pygraphviz
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
#import csv

#Define the BinarySearchTreeNode
class BSTNode:
    def __init__(self, key, left=None, right=None, parent=None):
        """Create a leaf node"""
        self._key = key
        self._left = left
        self._right = right
        self._parent = parent
        
    def __repr__(self):
        return str(self._key)

#Define the function to make a BST given preorder
def makeTree(preorder):
    """Returns a reference to the root of a binary search tree
    
    preorder: preorder sequence of labels in the BST
    """
    inorder = ''.join(sorted(preorder))
    if len(preorder)==0 and preorder==inorder:
        return None
    elif len(preorder)==1 and preorder==inorder:
        return BSTNode(preorder)
    else:
        rootLabel = preorder[0]
        ix = inorder.index(rootLabel)
        left_st = makeTree(preorder[1:1+ix])
        right_st = makeTree(preorder[1+ix:])
        node = BSTNode(rootLabel, left_st, right_st, None)
        if left_st:
            left_st._parent = node
        if right_st:
            right_st._parent = node
        return node

#Define the function to draw the tree given the root node
tmp = 0
def drawTree(node):
    """Returns a graphviz representation (string) of the tree
    rooted at node
    
    node: a BST node
    """
    def hiddenEdge(rootLabel):
        global tmp
        stLabel = 'x'+str(tmp)
        tmp += 1
        s = "{0} [style=invis]\n".format(stLabel)
        s += "{0} -> {1} [style=invis];\n".format(rootLabel, stLabel)
        return s
    s = ''   
    if not(node._left) and not(node._right): # leaf node
        return s
    if node._left:
        s1 = "{0} -> {1};\n".format(node._key, node._left._key)
        s1 += drawTree(node._left)
        s += s1
    else:
        s += hiddenEdge(node._key)
    if node._right:
        s2 = "{0} -> {1};\n".format(node._key, node._right._key)
        s2 += drawTree(node._right)
        s += s2
    else:
        s += hiddenEdge(node._key)
    return s

#Testing
t = makeTree(preorder="EDBACHFGIJ")  # E is the root!
#t = makeTree(preorder="BAC")  # E is the root!

print(drawTree(t))

drawing = open("tree.dot", 'w')
drawing.write('digraph { \n' + drawTree(t) + '\n}\n')
drawing.close()

#t1= nx.DiGraph(nx.drawing.nx_agraph.read_dot('tree.dot'))
#pos=nx.drawing.nx_agraph.graphviz_layout(t1, prog='dot')
#nx.draw(t1, pos, with_labels=True, arrows=True) 


def rotateLeftAt(bst):
    """Returns a reference to the root node of the subtree
    that results from performing a left rotation at the root of bst
    
    bst: the root of a binary search (sub)tree that has a right child
    """
    newRoot = None
    while bst._right:
        #code to rotate left
        newRoot = bst._right 
        NRRight = newRoot._left 
        newRoot._left = bst 
        bst._right = NRRight
        bst = newRoot
    if newRoot:
        newRoot._parent = bst._parent
        return newRoot
    return bst

"""
    while bst._right:
        #code to rotate left
        newRoot = bst._right 
        NRRight = newRoot._left 
        newRoot._left = bst 
        bst._right = NRRight
        newRoot._parent = bst._parent

        bst = newRoot

    return bst
"""

def leftistTree(bst):
    """Convert bst to return a reference to the root node of 
    corresponding leftist tree

    bst: root node of the bst (not null)
    """
    if bst:
        bst = rotateLeftAt(bst)
    if bst._left:
        leftistTree(bst._left)
    return bst


def isLeftist(t):
    """Checks if t is a leftist bst"""
    if not(t._left) and not(t._right):
        return True
    if t._right:
        return False
    return isLeftist(t._left)

t2 = leftistTree(t)
print(isLeftist(t2))  # should return True!

import csv
def make_graph(file):
    """Returns a networkx undirected graph
    
    file: a csv specification of a graph
    """
    csv_reader = csv.reader(file, delimiter=',')
    graph = nx.Graph()
    for line in csv_reader:
        state1 = line[0]
        state2 = line[1]
        if not graph.has_node(state1):
            graph.add_node(state1)
        if not graph.has_node(state2):
            graph.add_node(state2)
        graph.add_edge(state1, state2)
    return graph


f = open("/Users/dhondiyal/Downloads/neighbors-states.csv")
graph = make_graph(f)


def color(g, node, color_list, colors_of_nodes):
    for color in color_list:
        for neighbor in g.neighbors(node):
            if colors_of_nodes.get(neighbor, None) == color:
                return color

    
def six_coloring(g):
    """Returns a 6-coloring of g as a list of colors
    
    g: networkx undirected graph known to be planar
    """
    n = len(g.nodes())//6 + 1
    color_list = ['red', 'purple', 'green', 'orange', 'blue', 'yellow']*n
    color_list = color_list[:len(g.nodes())]
    colors_of_nodes = {}
    #Kempe's algorithm
    i = 0
    for node in g.nodes():
        color_list[i] = color(g, node, color_list, colors_of_nodes)
        i += 1
    return color_list

six_coloring(graph)