from pathlib import Path

print("| by using this you can find out the particular file ---- you entered ---- your need to enter the file type only like '.py , .txt , .js , etc' enter there |")
a = input("enter the path where you want to find the file  :")
b = input("enter the file name :")
for file in Path(a).rglob(f"{b}.*"):
 print(file)