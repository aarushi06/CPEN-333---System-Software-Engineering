# student name: Aarushi Mehra
# student number: 82519695
import math

def solveQuadratic(a: float, b: float, c: float) -> str:
    """
        This function takes the coefficients of a 
        quadratic equation as its three parameters.
        It returns a string that states its roots as
        described in the specification.
    """
    discriminant : float = math.pow(b, 2) - 4*a*c
    if discriminant < 0:  #The case for no real roots
        return ("No real roots")
    
    elif discriminant == 0:  #The case for one real root
        x: float = -b/(2*a)
        string_to_return: str = "The root is " + f"{x:.2f}" 
        return string_to_return
    
    elif discriminant > 0:  #The case for two real roots
        x1: float = (-b + math.sqrt(discriminant))/(2*a)
        x2: float = (-b - math.sqrt(discriminant))/(2*a)
        string_to_return: str = "The roots are " + f"{x1:.2f} " + "and " + f"{x2:.2f}"
        return string_to_return
        
    return ("To implement")
        
if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Do not limit your testing to these test cases.
        Make sure that you fully test your code.
    """
    Tests = [(1, 2, 3), (1, 2, 1), (1, 3, 1), (1.5, -8, -0.2)] 
    expectedOutput = ["No real roots", 
                      "The root is -1.00",  
                      "The roots are -0.38 and -2.62",
                      "The roots are 5.36 and -0.02"]
    for i in range(len(Tests)):
        print(f"Test {i} : a={Tests[i][0]}, b={Tests[i][1]} c={Tests[i][2]}")
        result = solveQuadratic(a=Tests[i][0], b=Tests[i][1], c=Tests[i][2])
        print(result)
        assert(result == expectedOutput[i])
