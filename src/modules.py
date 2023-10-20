from clear import clear # installed  clear
import os
import pandas as pd


# from keyboard_listener import KeyboardListener, Combo, KeyWord # Installed pynput

class MenuLogo():
    def __init__(self):
        self.logo ='''

        (                                                                                        
        )\ )   (                   )       (                   (          (                      
        (()/(   )\      )        ( /(       )\       )   (      )\ )       )\                     
        /(_)) ((_)  ( /(   (    )\())    (((_)   ( /(   )(    (()/(    ((((_)(    `  )    `  )   
        (_))_|  _    )(_))  )\  ((_)\     )\___   )(_)) (()\    ((_))    )\ _ )\   /(/(    /(/(   
        | |_   | |  ((_)_  ((_) | |(_)   ((/ __| ((_)_   ((_)   _| |     (_)_\(_) ((_)_\  ((_)_\  
        | __|  | |  / _` | (_-< | ' \     | (__  / _` | | '_| / _` |      / _ \   | '_ \) | '_ \) 
        |_|    |_|  \__,_| /__/ |_||_|     \___| \__,_| |_|   \__,_|     /_/ \_\  | .__/  | .__/  
                                                                                |_|     |_|     
                                                                    
        '''

        self.greeting = ("Welcome to the Flash Card App , customize your study and start now ! \n")
        self.options = '''

        [ 1 ] = Study a Deck

        [ 2 ] = Create a Deck / Create a Card

        [ 3 ] = Edit a Deck / Edit a Card

        [ 4 ] = Exit the app


        '''




class Main(MenuLogo):
    def __init__(self):
        super().__init__()
        
        print(self.logo)
        print(self.options)
        print(self.greeting)

        user_main_choice = int(input("\nPlease choose your option and hit enter: "))

        match user_main_choice:

                case 1:
                    StudyMenu()
                    
                # case 2:
                #     pass # Create a deck

                # case 3: 
                #     pass # Edit a deck

                # case 4: 
                #     pass # Exit app
                 

class StudyMenu(MenuLogo):
    def __init__(self):
        super().__init__()

        print(self.logo)
        self.greeting = ("Please choose from list\nPlease go to 'Edit a Deck' to change card amount")
        self.options = '''

        [ 1 ] = LIST OF DECKS TO CHOOSE


        '''

        print(self.greeting)
        print(self.options)


decks = {"Korean Example Deck": [{'card_num': 1, 'tot_daily_deck_count': 2, 'content': 'Hello', 'answer': '안녕하세요 (annyeonghaseyo)'}, {'card_num': 2, 'tot_daily_deck_count': 2, 'content': '안녕하세요 (annyeonghaseyo)', 'answer': 'Hello'}]}

def create_deck_from_file():
    
    new_deck =[]

    file_path = input("Enter the path or name of the text file: ")

    if os.path.isfile(file_path):
        with open(file_path, 'r') as c:
            lines = c.readlines()
    else:
        print("File not found. Please ennter a valid file path or name")


    for index,line in enumerate(lines):
        content, answer = line.strip().split(', ')
        index += 1
        card_info = {
            "card_num": index * 2,  # card number (unique)
            "tot_daily_deck_count": len(lines) * 2,  # out of the total cards to learn from today
            "content": content,  # content / Question
            "answer": answer,  # Answer
        }
        new_deck.append(card_info)

    for index,line in enumerate(lines):
        content,answer = line.strip().split(', ')
        index += 1
        card_info = {
            "card_num": index * 2 - 1,  # card number (unique)
            "tot_daily_deck_count": len(lines) * 2,  # out of the total cards to learn from today
            "content": answer,  # content swapped to create another card
            "answer": content,  # answer Swapped to create another card
        }
        new_deck.append(card_info)

    new_name = input("what do you want to name the deck?: ")

    if new_name not in decks:
        decks[new_name] = new_deck


    return decks  


def study_menu(decks):
    # study_menu_template = [0, deck_name, len(deck_name) , 0] # number , Name, total cards in deck, Daily cards to learn
    for k,v in decks.items():
        print (f'''
             
        - { k } | Cards to Study :   {len(v)}


     ''')

# Allows Study to happen

class ShowCard:
    def __init__(self, front, back):
        self.front = front
        self.back = back





