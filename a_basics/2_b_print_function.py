"""
    Q. What is Print Function ?  
        The print() function prints the given object to the standard output device (screen) or to the text stream file.
    
    -----------------------------------------------------------------------------------------------------
    
    Q. Write Syntax of Print ?  
        print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    
    -----------------------------------------------------------------------------------------------------

    Q. What is separator in print function ?  
        The `sep` (separator) parameter in the print function defines the string that separates multiple objects.  
        By default, it is a single space (' ').

        Example:  
            print("Hello", "World", sep="-")  
            Output: Hello-World  
    
    -----------------------------------------------------------------------------------------------------

    Q. What is flush in print function ?  
        The `flush` parameter controls whether output is forcibly written (flushed) immediately.  
        By default, `flush=False`, meaning output is buffered. Setting `flush=True` forces immediate output.  

    Example:  
    import time  
    print("Loading...", end="", flush=True)  
    time.sleep(3)  
    print(" Done!")  
        
    -----------------------------------------------------------------------------------------------------

    Q. What is Buffer ?  
    A buffer is a temporary storage area in memory that holds data before  
    it is processed or transferred to another location. In the context of printing in Python,  
    buffering is used to store output temporarily before displaying it on the screen or  
    writing it to a file.

    Output:  
    Loading... (waits for 3 seconds) Done!

    Q. What is file in print statement ?  
    The `file` parameter specifies where the output should be printed. By default, it is `sys.stdout` (the console),  
    but you can redirect output to a file.  

    Example:  
    with open("output.txt", "w") as f:  
        print("Hello, File!", file=f)  

    This writes "Hello, File!" into `output.txt` instead of printing it on the screen.
"""

# ================================================ CODING ================================================

# 1. Print "Hello Awanish"

print("Hello, Awanish")

# 2. Print Hello Golu in Text File (output.txt)

custom_file = open("file.txt", "w")
print("Hello, Awanish", file=custom_file)

# 3. Print Hello awanish using sep 

print("Hello", "Awanish", sep=', ')

# 3. Print table of 2 conditon "flush = False" while execution.

import time

num = 2
for table in range(10):
    print(num * (table+1), flush=False)


# 4. Print table of 2 conditon "flush = True" while execution.

import time

for number in range(50):
    print(number+1, flush=True)