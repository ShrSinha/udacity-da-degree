def swap(iList,i,j):
    iList[i], iList[j] = iList[j], iList[i]


def heapify(iList,parent,end):
    #heapify(input_list, parent_index, length_of_list)
    #Building Max Heap
    p = parent
    lc = 2 * parent + 1
    rc = 2 * parent + 2
    if lc < end and iList[p] < iList[lc]:
        p = lc
    if rc < end and iList[p] < iList[rc]:
        p = rc
    if p != parent:
        swap(iList,parent,p)
        heapify(iList,p,end)


def heapsort(iList):
    end = len(iList)
    least_parent = end // 2 - 1 
    for i in range(least_parent, -1, -1 ):
        heapify(iList,i,end)
    for i in range(end-1,0,-1):
        swap(iList,0,i)
        heapify(iList,0,i)
    return iList[-1]
    
    
print(heapsort([-1,3,3,4,5,6,7,8,0,0,0,1]))    