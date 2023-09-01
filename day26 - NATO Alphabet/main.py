import pandas
# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dictionary = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word to translate into NATO\nInput: ').upper()
nato_word = [nato_dictionary[letter] for letter in user_input if letter in nato_dictionary]
print(f'{user_input} == {nato_word}')
