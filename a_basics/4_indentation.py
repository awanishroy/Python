"""
    Q. What is Indentation in Python?  
    Indentation refers to spaces or tabs at the beginning of a line in Python.  
    Unlike other programming languages, Python uses indentation to define blocks of code instead of curly braces `{}`.

    Example:
    if True:
        print("This line is indented")  # This is inside the if block

    Q. Why is Indentation Important in Python?  
    - Python **requires** indentation; incorrect indentation will cause an `IndentationError`.  
    - It improves **code readability**.  

    Example (Correct Indentation):
    def greet():
        print("Hello!")  # Properly indented inside the function

    greet()

    Example (Incorrect Indentation - Will cause an error):
    def greet():
    print("Hello!")  # Error! Indentation is missing.

    Q. How Many Spaces Should Be Used for Indentation?  
    - The **standard** is **4 spaces per indentation level** (recommended by PEP 8).  
    - Avoid mixing spaces and tabs.  

    Example:
    for i in range(3):
        print(i)  # 4 spaces before print()

    Q. Where is Indentation Used?  
    - Inside functions, loops, conditionals, and classes.  

    Example:
    def example():
        if True:
            for i in range(2):
                print("Indented correctly")  # Nested indentation

    Q. What Happens If Indentation is Inconsistent?  
    - Python will raise an `IndentationError`.  

    Example:
    if True:
        print("Line 1")
      print("Line 2")  # Error! Inconsistent indentation.

    Q. Best Practices for Indentation  
    - Always use **4 spaces** (avoid tabs).  
    - Be consistent throughout your code.  
    - Use an IDE or text editor that supports automatic indentation (e.g., VS Code, PyCharm).  
    
"""
