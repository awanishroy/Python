"""
    Q. What is the input() Function in Python?  
        The `input()` function is used to take user input from the keyboard as a string.  
        It pauses program execution until the user provides input and presses Enter. 

    -----------------------------------------------------------------------------------------------------

    Q. What Data Type Does input() Return?  
    - `input()` always returns a string (`str`) by default.  
    - If numeric input is required, conversion is necessary.  
    
    -----------------------------------------------------------------------------------------------------

    Q. How to Take Integer or Float Input?  
    - Use `int()` for integers and `float()` for decimal values.  

    Example:
    num1 = int(input("Enter an integer: "))  # User enters 10
    num2 = float(input("Enter a decimal number: "))  # User enters 5.5
    print(num1 + num2)  # Output: 15.5

    Q. How to Take Multiple Inputs in One Line?  
    - Use `split()` to take multiple inputs at once.  

    Q. How to Set a Default Value for input()?  
    - Use conditional logic to provide a default value if no input is given.  

    Q. How to Handle input() with a Custom Separator?  
    - `split(",")` can be used to take comma-separated input.  

    Q. Best Practices for Using input()  
    - Always **convert** input when expecting numeric values.  
    - Use `strip()` to remove extra spaces (`input().strip()`).  
    - Provide **clear prompts** to users.  
    - Handle errors using `try-except` for unexpected input.  

"""

# ================================================ CODING ================================================

# 1. Take Input "Hello World"

# message = input("Enter 2 number with space to add")
# print(message)


# 2. Take input 2 number and add them

num_1, num_2 = map(int, input().split())
sum_result = num_1 + num_2

print(sum_result)


