from pathlib import Path
path_input=input("enter the path name :")
path = Path(path_input)
path.mkdir(exist_ok=True)
print("directory is created")
print("-----------------")
print("let's create file in the directory ")
a = input("enter the path:")
b = input("enter the file name:")
pathf = Path(a) / b
pathf.touch(exist_ok=True)
print("your file is created new")




