file_name="names.txt"
with open(file_name,'r')as file:
    content=file.read()
    print("File content: ")
    print(content)