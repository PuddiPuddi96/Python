#Open and read a file
# with open(file="../files/my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

#Open and write in a file. create the file if it doesnt exist
# with open(file="../files/my_file.txt", mode="w") as file:
#     file.write("Some text!")

#Open adn append some text in a file
with open(file="../files/my_file.txt", mode="a") as file:
    file.write("\nSome text!")
