'''
HeapOperation.py
Created on Feb 20, 2013
@author: Adriel Klein

The functions in this module are heap operations. These functions
are called to perform the extractMin and changeKey operations used
during Prim's algorithm.
'''

#Extracts the Node with the lowest attachment cost
#Puts element at heap[len(heap)-1] to heap[0] and performs heapify down
#Adjusts the heapMap according to any changes made in the heap
def extractMin(heap, heapMap):
    pair = heap[0]
    cost = pair[0]
    newTreeMember = pair[1]
    heapMap[newTreeMember] = -1 #Mark popped node as part of tree
    if len(heap) == 1:
        heap.pop()
        return pair

    heap[0] = heap[len(heap)-1]  # Move last node of heap to beginning
    heap.pop()
    heapMap[heap[0][1]] = 0 # Update heapMap for new first element
    heapifyDown(heap, heapMap, 0) # Send the first element of heap down to preserve properties of heap.
    return pair

#Changes the key of a key-value pair in the heap
def changeKey(heap, heapMap, node, newKey):
    heapIndex = heapMap[node]
    heap[heapIndex] = (newKey, heap[heapIndex][1])
    heapifyUp(heap, heapMap, heapIndex)
    
def heapifyDown(heap, heapMap, i):
    lastHeapPosition = len(heap) - 1
    leftChild = 2*(i + 1) -1
    rightChild = leftChild + 1
    if leftChild > lastHeapPosition:
        # Cannot heapify anymore. Update heapMap and terminate. 
        currentNode = heap[i][1]
        heapMap[currentNode] = i 
        return
    elif leftChild < lastHeapPosition:
        minChild = 'child with lower heap value'
        if heap[leftChild][0] < heap[rightChild][0]:
            minChild = leftChild
        else:
            minChild = rightChild
    elif leftChild == lastHeapPosition:
        minChild = leftChild
    
    if heap[i][0] > heap[minChild][0]:
        #Swap the array entries heap[i] and heap[minChild]
        temp = heap[minChild]
        heap[minChild] = heap[i]
        heap[i] = temp
        #Update heapMap
        heapMap[heap[i][1]] = i
        heapMap[heap[minChild][1]] = minChild
        heapifyDown(heap, heapMap, minChild)

def heapifyUp(heap, heapMap, i):
    if i == 0: # Cannot heapify anymore. Update heapMap and terminate
        heapMap[heap[0][1]] = 0
        return
    parent = i/2
    if heap[parent][0] > heap[i][0]:
        # Swap parent and child.
        temp = heap[i]
        heap[i] = heap[parent]
        heap[parent] = temp
        #Update heapMap
        heapMap[heap[i][1]] = i
        heapMap[heap[parent][1]] = parent
        heapifyUp(heap, heapMap, parent)

    
    