# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACE_HOLDER = '[name]'
LETTER_NAME = 'letter_for'
STARTING_LETTER = './Input/Letters/starting_letter.txt'
INVITE_LIST = './Input/Names/invited_names.txt'

# Read starting letter
with open(file=STARTING_LETTER, mode='r', encoding='utf8') as letter:
    text = letter.read()

# Read invite list
with open(file=INVITE_LIST, mode='r', encoding='utf8') as invite_list:
    name_list = invite_list.read().split('\n')

# Create invitation
for name in name_list:
    letter = text.replace(PLACE_HOLDER, name)
    with open(file=f'./Output/ReadyToSend/{LETTER_NAME}_{name.lower()}.txt', mode='w', encoding='utf8') as output:
        output.write(letter)

