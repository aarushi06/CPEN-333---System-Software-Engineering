#student name: Aarushi Mehra
#student number: 82519695

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """

    # print(f"Thread {threading.current_thread().name}")  for testing purposes 

    #global sortedFirstHalf   #assigning scope of the list variables 
    #global sortedSecondHalf
    
    split = len(testcase)//2    #splitting the testcase list into two lists 
    sort_first = []
    sort_second = []
    sort_first = testcase[0:split]
    sort_second = testcase[split:]
    def SortArray(array):             #inner function implementation of bubble sort
        for i in range(len(array)):
            for j in range(len(array)-1):
                if (array[j] > array[j+1]):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array

    if (firstHalf == True):     #sort the first half of the array if the parameter firstHalf is True
        SortArray(sort_first)
        sortedFirstHalf = sort_first
        
    else:                                 #otherwise if parameter firstHalf is False, sort the second half of the array
        SortArray(sort_second)
        sortedSecondHalf = sort_second

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    print(f"Thread {threading.current_thread().name}")
   # global SortedFullList
    i = 0 
    j = 0

    while(i<len(sortedFirstHalf) and j<len(sortedSecondHalf)):
        if (sortedFirstHalf[i] <= sortedSecondHalf[j]):
            SortedFullList.append(sortedFirstHalf[i])
            i+= 1

        elif(sortedFirstHalf[i] > sortedSecondHalf[j]):
            SortedFullList.append(sortedSecondHalf[j])
            j+= 1

    while(i<len(sortedFirstHalf)):                  #to append the remaining of the lists 
        SortedFullList.append(sortedFirstHalf[i])
        i = i + 1

    while(j<len(sortedSecondHalf)):
        SortedFullList.append(sortedSecondHalf[j])
        j = j + 1
    

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    

    thread1 = threading.Thread(target = sortingWorker, args = (True,))
    thread2 = threading.Thread(target = sortingWorker, args = (False,))
    thread3 = threading.Thread(target = mergingWorker)
    
    thread1.start()
    thread2.start()

    print('Firsthalf: ', sortedFirstHalf)    #for testing
    print('Secondhalf: ', sortedSecondHalf)  #for testing
    thread1.join()
    thread2.join()

    thread3.start()
    thread3.join()
 
    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)
  