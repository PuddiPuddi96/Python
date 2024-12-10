import pandas

alphabet_data_frame = pandas.read_csv("./data/nato_phonetic_alphabet.csv")
alphabet_dictionary = {row.letter:row.code for (_, row) in alphabet_data_frame.iterrows()}

def generate_phonetic():
    word_from_user = input("Enter a word: ").upper()
    try:
        result = [alphabet_dictionary[letter] for letter in word_from_user]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
