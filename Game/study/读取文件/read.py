with open("te/file.txt") as file_object:
    content = file_object.read()
    for line in file_object:

        print(line)
