import random_word_generator

def change_current_word_state(selected_word,current_word_state,character):
    modified_word_state = ""
    for i in range(len(selected_word)):
        if current_word_state[i] == "_" and selected_word[i] == character:
            modified_word_state += character
        else:
            modified_word_state += current_word_state[i]    

    return modified_word_state   
 
def input_character_in_word(selected_word, input_char, current_word_state, attempts_remaining):
    if input_char in selected_word:
        current_word_state = change_current_word_state(selected_word, current_word_state, input_char)
    else:
        attempts_remaining -= 1
    return current_word_state, attempts_remaining 
def print_current_state(current_word_state,attempts_remaining):

    """ printing current condition of user """
    
    print("Current State: ",end=" ")

    for i in current_word_state:
        print(i,end=" ")
     print("\tAttempts Remaining : {}".format(attempts_remaining)) 