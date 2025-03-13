# file = open("xyz.txt","r+")

# some_text = file.read()

# print(some_text)


import os 
# cwd = os.getcwd() 
# print("Current working directory:", cwd) 

# path = os.path.join(cwd, "testing.txt")

# print(os.mkdir(path))

# print("diretory %s created" %path, "Successfully" )
with open("createdfile.txt", "w") as f:
    f.write("Created using write mode.")