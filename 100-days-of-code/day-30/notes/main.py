# File not found
# try:
#     file = open("temp_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["a_key"])
# except FileNotFoundError:
#     file = open("temp_file.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} doesnt exist")
# else: # When try is ok
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error that I made up") # For own exception

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
