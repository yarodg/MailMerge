PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt", mode="r") as file_names:
    names = file_names.readlines()

with open(f"./Input/Letters/starting_letter.txt") as file_letter:
    letter_contents = file_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
