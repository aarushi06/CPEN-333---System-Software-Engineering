# student name: Aarushi Mehra
# student number: 82519695
def displayPyramid(size: int) -> None:
    """
        This method prints a pyramid of size size.
        Implement the method using nested for loops.
        size is an integer between 1 and 9 (inclusive).
        Example: if size is 7, it should print:
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
    """      
    x = ' '
    for i in range(1, size+1):
        print((x*(size*2 - 2*i)), end = " ")   #printing spaces before the line begins
        for j in range(0, i):
            print (i - j, end = " ")   #decrease till 1
        for k in range(1, i):
            print (k + 1, end = " ")   #increase from 1
        print("\n")
    
        
if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Make sure that you fully test your code.
        This prints the output for all rquired 
        sizes, from 1 to 9.
    """
    for size in range (1, 10):
        displayPyramid(size)
