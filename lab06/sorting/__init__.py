#Jonathan Ong 
def mo3_quicksort(alist):
    #helps find the median
    def mo3_picker(alist, first,last):
        mid = (first+last)//2
        if max(alist[first],alist[last]) <= alist[mid] <= min(alist[0],alist[last]):
            return alist[mid] , mid
        elif max(alist[first],alist[mid]) <= alist[last] <= min(alist[0],alist[mid]):
            return alist[last] , last
        else:
            return alist[first] , first

    #call partion using median value
    def mo3_partition(alist,first,last):

        pivotvalue, pivotx = mo3_picker(alist,first,last)
        leftmark = first +1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
           
            pivotvalue = alist[first]

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1

            if rightmark <= leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

            temp = alist[first]
            alist[first] = alist[rightmark]
            alist[rightmark] = temp


        return rightmark
    #uses chapter 5.12 helper function to partion array list
    def mo3_quickSortHelper(alist,first,last):
        if first<last:
            splitpoint = mo3_partition(alist,first,last)

            mo3_quickSortHelper(alist,first,splitpoint-1)
            mo3_quickSortHelper(alist,splitpoint+1,last)
    mo3_quickSortHelper(alist,0,len(alist)-1)
#------------------------(5.12 code)--------------------------
def quickSort(alist):
    def quickSortHelper(alist,first,last):
        if first<last:

            splitpoint = partition(alist,first,last)

            quickSortHelper(alist,first,splitpoint-1)
            quickSortHelper(alist,splitpoint+1,last)


    def partition(alist,first,last):
        pivotvalue = alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp


        return rightmark
    quickSortHelper(alist,0,len(alist)-1)


#tests
#alist02= [7,2,1,6,3,4,5,3,2,8]
#alist = [54,26,93,17,77,31,44,55,20]
#quickSort(alist)
#mo3_quicksort(alist02)
#print(alist)
#print(alist02)