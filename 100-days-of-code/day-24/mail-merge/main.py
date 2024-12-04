PLACEHOLDER = "[name]"

letter_contents = ""
with open(file="input/letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read().strip()

names = []
with open(file="input/names/invited_names.txt", mode="r") as names_file:
    for name in names_file.readlines():
        names.append(name.strip())

for name in names:
    new_letter = letter_contents.replace(PLACEHOLDER, name)
    file_name = f"letter_for_{name}.txt"
    with open(file="output/readyToSend/" + file_name, mode="w") as new_file:
        new_file.write(new_letter)
