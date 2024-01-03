import random_word_generator

def change_current_word_state(selected_word,current_word_state,character):
    modified_word_state = ""
    for i in range(len(selected_word)):
        if current_word_state[i] == "_" and selected_word[i] == character:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]    

    return modified_word_state    