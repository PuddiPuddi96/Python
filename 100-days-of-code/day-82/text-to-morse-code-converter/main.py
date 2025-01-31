MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def get_input_text() -> str:
    text = ''
    while(not text):
        text = input('Type text to convert: ').upper()
    return text

def from_text_to_morse_code(text:str) -> str:
    morse_code_text = ''
    for char in text:
        if char != ' ':
            try:
                # 1 space indicates different characters
                morse_code_text += MORSE_CODE_DICT[char] + ' '
            except (KeyError):
                print(f'The character {char} cannot be translated into morse code')
        else:
            # 2 indicates different words
            morse_code_text += ' '
    return morse_code_text

def main():
    text = get_input_text()
    morse_text = from_text_to_morse_code(text)
    print(morse_text)

if __name__ == '__main__':
    main()
