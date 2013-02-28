'''
UnitSquareMST.py
Created on Feb 21, 2013
@author: adrielklein

This program will use Prim's algorithm to find the weight of a minimum spanning tree of a complete graph 
with n vertices, where the vertices are points chosen uniformly at random inside the unit square. The 
weight of an edge is the Euclidean distance between endpoints.
'''
from random import uniform #Required to find uniform value in range(0,1)
from HeapOperations import extractMin, changeKey, heapifyUp, heapifyDown
from heapq import heapify
from math import sqrt #Required to take square root.

#Returns a set of n points in the unit square
def createPointsInUnitSquare(n):
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def getOrderedPair(self):
            return (self.x, self.y)
    points = []
    for i in range(n):
        points.append(Point(uniform(0, 1), uniform(0, 1)))
    return points
# Returns the squared distance between two points
def squaredDistance(point1, point2):
    x1, y1 = point1.getOrderedPair()
    x2, y2 = point2.getOrderedPair()
    return (y2 - y1)**2 + (x2 - x1)**2

# Creates an adjacency matrix with
def createAdjacencyMatrix(n):
    points = createPointsInUnitSquare(n)
    def getRow(i):
        #Compute distances from ith node
        focalPoint = points[i]
        newRow = [squaredDistance(focalPoint, points[j]) for j in range(i)]
        newRow.append(0.0)
        return newRow
    adjacencyMatrix = [getRow(i) for i in range(n)]
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
    return sqrt(treeWeight)


print "Nodes: MST Weight"
#The following loop runs the algorithm for various input lengths and prints the results.
for x in range(4, 14):
    weights = []
    for j in range(5):
        weights.append(minimumSpanningTreeWeight(2**x))
    print str(2**x) + ": " + str(sum(weights)/ 5.0)
