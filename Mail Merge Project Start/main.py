#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import random,shutil

#per path relativo(cioe non parte da root C:, usa ./path)
#per creare un nuovo file basta come cercarlo
# listnames = []
# listnamesfiles = []
# with open("./Input/Names/invited_names.txt") as names_file:
#     for line in names_file:
#         listnames.append(line)
#     print(listnames)
# for index,_ in enumerate(listnames):
#     namefile = f"myletternum{index}.txt"
#     listnamesfiles.append(namefile)
#
# with open("./Input/Letters/starting_letter.txt") as originalletter:
#     original_content = originalletter.read()
#
# for name in listnames:
#     update_content = original_content.replace("[name]", name)
#
# for index,letter in enumerate(listnamesfiles):
#     test = open (f"./Input/Letters/{letter}", mode="w")
#     update_content = original_content.replace("[name]", listnames[index])
#     test.write(update_content)

PLACEHOLDER = "[name]"
with open ("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open ("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open (f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



