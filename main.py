student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# phonetics_code_words = list(new_dict.values())
# phonetics_code_words = [code_word for code_word in new_dict.values()]
# print(phonetics_code_words)

def generate_nato():
    answer = input("Enter a word: ")
    letter_list = [letter.upper() for letter in answer]
    try:
        code_word_list = [new_dict[letter] for letter in letter_list]
    except KeyError:
        print("Please enter only letters from the alphabet")
        generate_nato()
    else:
        print(code_word_list)


generate_nato()

