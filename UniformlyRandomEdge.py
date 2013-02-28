'''
UniformlyRandomEdgeMST.py
Created on Feb 18, 2013
@author: adrielklein

This program will use Prim's algorithm to find the weight of a minimum spanning tree of a complete graph
with n vertices, where the weight of each edge is a real number chosen uniformly at random from [0, 1].

'''

from random import uniform #Required to find uniform value in range(0,1)
from HeapOperations import extractMin, changeKey, heapifyUp, heapifyDown
from heapq import heapify

# Creates and an adjacency matrix of n nodes with undirected edges.
# The adjacency matrix has (1/2)n^2 entries to conserve memory. Note that
# this is only possible since edges are undirected. The edge weights are 
# chosen uniformly at random in interval (0, 1). The i-th row of the matrix
# represents the edge weight from node i to other nodes in the graph.
def createAdjacencyMatrix(n):
    def getRow(i):
        newRow = [uniform(0, 1) for j in range(i)]
        newRow.append(0.0)
        return newRow  
     
    adjacencyMatrix = [ getRow(i) for i in range(n)]
    return adjacencyMatrix


def minimumSpanningTreeWeight(n):
    adjacencyMatrix = createAdjacencyMatrix(n)
    # Node 0 will be the root node.
    distancesFromRoot = [adjacencyMatrix[i][0] for i in range(n)] #First column of matrix
    # Create heap where key is attachmentCost and value is the node.
    attachmentCosts = [(distancesFromRoot[i], i) for i in range(n)]
    heapify(attachmentCosts)
    
    #Create heapMap that maps each node to its position in heap
    heapMap = [None]*n
    #Populate heapMap
    for i in range(n):
        node = attachmentCosts[i][1]
        heapMap[node] = i
    
    treeWeight = 0
    while len(attachmentCosts) != 0:
        pair = extractMin(attachmentCosts, heapMap)
        cost = pair[0]
        newTreeMember = pair[1]
        treeWeight += cost
        
        # Change the keys of all the nodes in the heap that have a new attachment cost
        for i in range(n):
            if heapMap[i] != -1:
                if newTreeMember >= i:
                    possiblySmallerCost = adjacencyMatrix[newTreeMember][i]
                else:
                    possiblySmallerCost = adjacencyMatrix[i][newTreeMember]
                if possiblySmallerCost < attachmentCosts[heapMap[i]][0]:
                    changeKey(attachmentCosts, heapMap, i, possiblySmallerCost)
    return treeWeight

print "Nodes: MST Weight"
#The following loop runs the algorithm for various input lengths and prints the results.
for x in range(4, 14):
    weights = [minimumSpanningTreeWeight(2**x) for i in range(5)]
    print str(2**x) + ": " + str(sum(weights) / len(weights))