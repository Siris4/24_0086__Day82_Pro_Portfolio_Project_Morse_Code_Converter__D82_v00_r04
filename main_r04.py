# Siris's Text-to-Morse Code Converter:

print("##########################################################")
print("#                                                        #")
print("#    Welcome to Siris's Text-to-Morse Code Converter!    #")
print("#                                                        #")
print("##########################################################")


dot = "●"
dash = "▬▬"
space = " "
after_char_double_spacing = "   "
print('')

# print(f"This is a test: " + dot + space + dash)

sentence = 'Hello, are you my father?'  # account for any special chars

morse_code_dict = {
    'a': dot + space + dash + after_char_double_spacing,
    'A': dot + space + dash + after_char_double_spacing,
    'b': dash + space + dot + space + dot + space + dot + after_char_double_spacing,
    'B': dash + space + dot + space + dot + space + dot + after_char_double_spacing,
    'c': dash + space + dot + space + dash + space + dot + after_char_double_spacing,
    'C': dash + space + dot + space + dash + space + dot + after_char_double_spacing,
    'd': dash + space + dot + space + dot + after_char_double_spacing,
    'D': dash + space + dot + space + dot + after_char_double_spacing,
    'e': dot + after_char_double_spacing,
    'E': dot + after_char_double_spacing,
    'f': dot + space + dot + space + dash + space + dot + after_char_double_spacing,
    'F': dot + space + dot + space + dash + space + dot + after_char_double_spacing,
    'g': dash + space + dash + space + dot + after_char_double_spacing,
    'G': dash + space + dash + space + dot + after_char_double_spacing,
    'h': dot + space + dot + space + dot + space + dot + after_char_double_spacing,
    'H': dot + space + dot + space + dot + space + dot + after_char_double_spacing,
    'i': dot + space + dot + after_char_double_spacing,
    'I': dot + space + dot + after_char_double_spacing,
    'j': dot + space + dash + space + dash + space + dash + after_char_double_spacing,
    'J': dot + space + dash + space + dash + space + dash + after_char_double_spacing,
    'k': dash + space + dot + space + dash + after_char_double_spacing,
    'K': dash + space + dot + space + dash + after_char_double_spacing,
    'l': dot + space + dash + space + dot + space + dot + after_char_double_spacing,
    'L': dot + space + dash + space + dot + space + dot + after_char_double_spacing,
    'm': dash + space + dash + after_char_double_spacing,
    'M': dash + space + dash + after_char_double_spacing,
    'n': dash + space + dot + after_char_double_spacing,
    'N': dash + space + dot + after_char_double_spacing,
    'o': dash + space + dash + space + dash + after_char_double_spacing,
    'O': dash + space + dash + space + dash + after_char_double_spacing,
    'p': dot + space + dash + space + dash + space + dot + after_char_double_spacing,
    'P': dot + space + dash + space + dash + space + dot + after_char_double_spacing,
    'q': dash + space + dash + space + dot + space + dash + after_char_double_spacing,
    'Q': dash + space + dash + space + dot + space + dash + after_char_double_spacing,
    'r': dot + space + dash + space + dot + after_char_double_spacing,
    'R': dot + space + dash + space + dot + after_char_double_spacing,
    's': dot + space + dot + space + dot + after_char_double_spacing,
    'S': dot + space + dot + space + dot + after_char_double_spacing,
    't': dash + after_char_double_spacing,
    'T': dash + after_char_double_spacing,
    'u': dot + space + dot + space + dash + after_char_double_spacing,
    'U': dot + space + dot + space + dash + after_char_double_spacing,
    'v': dot + space + dot + space + dot + space + dash + after_char_double_spacing,
    'V': dot + space + dot + space + dot + space + dash + after_char_double_spacing,
    'w': dot + space + dash + space + dash + after_char_double_spacing,
    'W': dot + space + dash + space + dash + after_char_double_spacing,
    'x': dash + space + dot + space + dot + space + dash + after_char_double_spacing,
    'X': dash + space + dot + space + dot + space + dash + after_char_double_spacing,
    'y': dash + space + dot + space + dash + space + dash + after_char_double_spacing,
    'Y': dash + space + dot + space + dash + space + dash + after_char_double_spacing,
    'z': dash + space + dash + space + dot + space + dot + after_char_double_spacing,
    'Z': dash + space + dash + space + dot + space + dot + after_char_double_spacing,
    ' ': '\n',
    ',': ',',
    '-': '-',
    '?': '?',
    '!': '!',

    # Numbers 0-9
    '0': dash + space + dash + space + dash + space + dash + space + dash + after_char_double_spacing,
    '1': dot + space + dash + space + dash + space + dash + space + dash + after_char_double_spacing,
    '2': dot + space + dot + space + dash + space + dash + space + dash + after_char_double_spacing,
    '3': dot + space + dot + space + dot + space + dash + space + dash + after_char_double_spacing,
    '4': dot + space + dot + space + dot + space + dot + space + dash + after_char_double_spacing,
    '5': dot + space + dot + space + dot + space + dot + space + dot + after_char_double_spacing,
    '6': dash + space + dot + space + dot + space + dot + space + dot + after_char_double_spacing,
    '7': dash + space + dash + space + dot + space + dot + space + dot + after_char_double_spacing,
    '8': dash + space + dash + space + dash + space + dot + space + dot + after_char_double_spacing,
    '9': dash + space + dash + space + dash + space + dash + space + dot + after_char_double_spacing
}

# Example usage:
# print(f"Morse code for 'a': {morse_code_dict['a']}")
# print(f"Morse code for 'A': {morse_code_dict['A']}")
# print(f"Morse code for '5': {morse_code_dict['5']}")
# print(f"Morse code for 's': {morse_code_dict['s']}")
# print(f"Morse code for 'z': {morse_code_dict['z']}")
# print(f"Morse code for 'r': {morse_code_dict['r']}")

full_sentence = ""

for char in sentence:
    full_sentence += morse_code_dict[char]

print(full_sentence)
# print(morse_code_dict[sentence])