# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file_write.txt", mode="a") as file:
    file.write("\nPlato2")
    print(contents)