from collections import defaultdict
import networkx as nx

def addNodes(line, graph, w):
    #add the information without the "\n", keep track of weight for each node
    graph.add_node(line[:len(line) - 2], weight = w)

def sidesMatch(firstNode, secondNode, graph):
    for number in firstNode.split():
        for otherNumber in secondNode.split():
            if number == otherNumber:
                return True
    return False

def setEdges(graph):
    for node in graph.nodes(data = True):
        for otherNode in graph.nodes(data = True):
            #if both are same node, do nothing
            if node == otherNode:
                continue
            #do not add an edge from light node to heavy node
            firstNode = graph.nodes(data = node[0])._data
            secondNode = graph.nodes(data = otherNode[0])._data
            #if an edge between two nodes already exists, dont add
            if graph.has_edge(secondNode, firstNode):
                continue
            #only add an edge between two nodes if they have a common surface
            if sidesMatch(firstNode, secondNode, graph):
                graph.add_edge(firstNode, secondNode)

def createTower(graph, case):
    array = list(nx.dag_longest_path(graph, default_weight = 1))
    length = len(array)

    print("Case ", case)
    print(length)

    previousCube = None
    previousWeight = 0
    counter = 0
    for element in array:
        #weight = which matrix are we looking at: this is to be printed
        weight = graph.nodes[element]['weight']
        if counter == 0:
            previousCube = element
            previousWeight = weight
            counter += 1
            continue
        #look for a match
        brk = False
        for x in previousCube.split():
            for y in element.split():
                if x == y:
                    brk = True
                    break
            if brk:
                break
        #get index of x
        for index in range(len(element.split())):
            if element[index] == x:
                index = index // 2
                break
        if index == 0:
            print(previousWeight, " back")
        elif index == 1:
            print(previousWeight, " front")
        elif index == 2:
            print(previousWeight, " right")
        elif index == 3:
            print(previousWeight, " left")
        elif index == 4:
            print(previousWeight, " bottom")
        elif index == 5:
            print(previousWeight, " top")
        previousCube = element
        previousWeight = weight
    
    if index == 0:
        print(previousWeight, " front")
    elif index == 1:
        print(previousWeight, " back")
    elif index == 2:
        print(previousWeight, " left")
    elif index == 3:
        print(previousWeight, " right")
    elif index == 4:
        print(previousWeight, " top")
    elif index == 5:
        print(previousWeight, " bottom")
    

def main():
    graph = nx.DiGraph()
    #open file, read line by line
    firstLine = False
    with open("/Users/dhondiyal/Downloads/input7.2.txt") as f:
        weight = 1
        case = 1
        #do  a while True because we want to perform the following actions repeatedly
        brk = False
        brk2 = False
        while True:
            line = f.readline()
            if brk2:
                break
            if(line == "0\n"):
                #end of file
                brk = True
            #if the current line describes cube
            if len(line.split()) > 2:
                #create ndoes and add
                addNodes(line, graph, weight)
                weight += 1
            #if the current line does not describe the cube (new test case)
            elif len(line.split()) < 2:
                weight = 1
                #if this is the first line, we cant print anything, so just skip
                if firstLine == False:
                    firstLine = True
                    continue
                #set edges
                setEdges(graph)
                #create the tower + output
                createTower(graph, case)
                case += 1
                graph.clear()
                print("")
                if brk:
                    brk2 = True

main()
