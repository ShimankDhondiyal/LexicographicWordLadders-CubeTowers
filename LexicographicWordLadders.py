from collections import defaultdict
import networkx as nx


def makeGraph(text):
    graph = nx.DiGraph()
    for word in text.split():
        graph.add_node(word)
    return graph

def isEditStep(firstWord, secondWord):
    firstWord = firstWord._data
    secondWord = secondWord._data
    #if the words are more than one letter greater/less, then it is not an edit step
    if abs(len(firstWord) - len(secondWord)) > 1:
        return False
    #if the words are the same length, keep track of how many letters are different
    elif len(firstWord) == len(secondWord):
        count = 0
        #iterate through firstword and secondword, compare letters
        firstLetterIndex = 0
        secondLetterIndex = 0
        while True:
            if firstLetterIndex == len(firstWord) or secondLetterIndex == len(secondWord):
                break
            if firstWord[firstLetterIndex] != secondWord[secondLetterIndex]:
                count += 1
            if count > 1:
                return False
            firstLetterIndex += 1
            secondLetterIndex += 1
        #at this point, both words traversed and no issue so true
        return True
    #else: word length is differenet by 1. the letters MUST be the same with the exception of the one extra letter
    else:
        if len(firstWord) > len(secondWord):
            larger = firstWord
            smaller = secondWord
        else:
            larger = secondWord
            smaller = firstWord
        count = 0
        smallerLetterIndex = 0
        largerLetterIndex = 0
        while True:
            if smallerLetterIndex == len(smaller):
                if largerLetterIndex == len(larger) - 1 and count == 0:
                    #there is only one letter left in word, no matter what it is, word is edit step
                    return True
                else:
                    return False
            if smaller[smallerLetterIndex] != larger[largerLetterIndex]:
                count += 1
                if count > 1:
                    return False
                if smallerLetterIndex == len(smaller) - 1:
                    return False
                if larger[largerLetterIndex + 1] == smaller[smallerLetterIndex + 1]:
                    largerLetterIndex += 1
                    smallerLetterIndex += 1
                    continue
                else:
                    largerLetterIndex += 1
                    continue
            smallerLetterIndex += 1
            largerLetterIndex += 1
        return True

def setEdges(graph):
    for node in graph:
        for otherNode in graph:
            #only do the following if the nodes are in alphabetical order
            #if an edge between two nodes already exists, dont add
            if graph.has_edge(node, otherNode) or (node >= otherNode):
                continue
            #else, if the two nodes are an edge step, then link them
            if isEditStep(graph.nodes(data = node), graph.nodes(data = otherNode)):
                graph.add_edge(node, otherNode)

def getLargest(graph):
    array = list(nx.dag_longest_path(graph, default_weight=1))
    length = len(array)
    print(length, ":", end = " ")
    for element in array:
        print(element, end = " ")

def main():
    text = "cat dig dog fig fin fine fog log wine"
    #make graph and input words as nodes
    graph = makeGraph(text)
    #link words based on whether or not they're edit-steps
    setEdges(graph)
    #call dfs on the graph to find the traversal wtith the most nodes
    getLargest(graph)

main()