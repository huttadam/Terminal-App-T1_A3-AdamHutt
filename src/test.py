import pytest
import modules

cd = modules.CreateDeckMenu()
md = modules.Main()

#Feature 1 - Studying through a deck of flashcard and checking if the responses are working as planned

#Test 1 - Case 1 

# Expecting:

# "z" is supposed to show the other side of the card

# "a" is the wrong answer and the total should increase buy 2 and the card repeat two more times
# "s" is the user wants to repeat the card once, so the total should increase by one and repeat one more time
# "d" the user is correct and the card will not repeat in the deck.

# "q" is to quit the deck , can only be done , after z is pressed (show card)

# z - works as expected
# a -works as expected
# s - works as expected
# d - works as expected
 
 # Explained further in slide deck (photos)

 # Test 2 - Case 2

 # Expecting: screen to reset and no card details to change, if user enters a key other than q,z,a,s,d

 # Works as expected 

 # Works as expected


#Feature 2 

# Creating Deck (through user file)  - Case -1 (error message)

# Expecting - will create a value error, return to menu and give user message

def test_for_mis_formatted_txt_from_user():
    with pytest.raises(ValueError):
        cd.create_deck_from_file

cd.test_for_mis_formatted_txt_from_user()

# # using test1_template.txt, it is mis-formatted with too many "/" (seperator)

# Creating Deck (through user file)  - Case -2 (works)

#Expecting - After adding src file, ask me for a name (Test2) and enter into Json deck

def test_for_txt_file_correct_upload():
    cd.create_deck_from_file()
    with open('decks.json', 'r') as json_file:
        decks = json.load(json_file)

    assert 'Test2' in decks

test_for_txt_file_correct_upload()



check_wrong_again_easy_functions()