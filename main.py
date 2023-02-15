import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
# nato_dict = nato_data.to_dict()
# print(nato_dict)

nato_dict = {row.letter: row.code for(index, row) in nato_data.iterrows()}

name = input(f"Enter a word: ").upper()
name_char = [nato_dict[char] for char in name]
# nato_list = [row.code for (index, row) in nato_data.iterrows() if row.letter in name_char]
# print(nato_list)
print(name_char)

# name = input(f"Enter a word: ").upper()
# name_char = [char for char in name]
# result = {n for letter, code in }

# result = [code for char in name if letter == char for letter, code in nato_dict.items()]
# print(result)





