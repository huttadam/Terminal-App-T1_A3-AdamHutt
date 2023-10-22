import data
from clear import clear # installed  clear
import os
from pynput.keyboard import Key, Listener
import random
import json


# ///////////////// Navigation / Menu's /////////////////

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
        clear()
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
        clear()
        print(self.logo)
        self.greeting = ("Please choose from list\n")


        print(self.greeting)


        with open('decks.json', 'r') as json_file:
            d = json.load(json_file)

        # print(d)

        deck_keys = []
        for json_deck in d:
            for key in json_deck.keys():
                deck_keys.append(key)

    
        print("Available Decks:\n")
        for i, key in enumerate(deck_keys, start=1):
            print(f"[ {i} ] {key}\n")

    
        selected_index = int(input("\nPlease choose with the number and hit enter: "))
        if 1 <= selected_index <= len(deck_keys):
            selected_deck = d[selected_index - 1] 
            CardFormatter.init_deck(selected_deck)
        else:
            print("Invalid choice. Please select a valid deck.")









# ///////////////// Create a Deck  /////////////////

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
            "content": content,  # content / Question
            "answer": answer,  # Answer
        }
        new_deck.append(card_info)

    for index,line in enumerate(lines):
        content,answer = line.strip().split(', ')
        index += 1
        card_info = {
            "content": answer,  # content swapped to create another card
            "answer": content,  # answer Swapped to create another card
        }
        new_deck.append(card_info)


    while True:
        new_name = input("What do you want to name the deck?: ")

        deck_exists = False


        for deck in data.decks:
            for key in deck.keys():
                if new_name == key:
                    deck_exists = True
                    break 

        if deck_exists:
            print("The deck name already exists.")

        else:
            data.decks.append({new_name: new_deck})
            print(f"Deck '{new_name}' has been created.")
            break
    print(data.decks)
    



def study_menu(decks):
    for k,v in decks.items():
        print (f'''
             
        - { k } | Cards to Study :   {len(v)}


     ''')

# ///////////////// Study a Deck /////////////////

class CardFormatter:
    def init_deck(deck):
            
        formatted_card_bank = []
            
        for k,v in deck.items():
            deck_name = k
            for card in v:
                card_front = card["content"]
                card_back = card["answer"]
                new_card = Card(card_front, card_back, deck_name)
                formatted_card_bank.append(new_card)

            study_deck = Study(formatted_card_bank)
            study_deck.card_display()



class Card:
    def __init__(self, front, back, deck_name):
        self.front = front
        self.back = back
        self.deck_name = deck_name


class Study:
    def __init__(self, for_deck):
        self.for_deck = for_deck
        self.card_num = 0
        # self.listener_active = False
        self.shuffled_deck = for_deck[:] 
        random.shuffle(self.shuffled_deck)

    def show_card(self):
        self.show_card_input = input("Press 'Z' and enter to show: ")

        if self.show_card_input == 'Z':
            self.show_answer_and_options()


    def progress_deck(self):
        self.next_card = input("Press 'A' 'S' or 'D': ")

        if self.next_card == 'A' or self.next_card == 'S':
            self.shuffled_deck.append(self.shuffled_deck[self.card_num])
            self.card_num += 1
            self.card_display()
        else:
            self.card_num += 1
            self.card_display()

            




    # def on_key_release(self, key):

    #     if key == Key.space:
    #         self.listener_active = True
    #         self.show_answer_and_options()
            
    #     elif key == Key.right:
    #         self.listener_active = True
    #         self.card_num += 1
    #         if self.card_num < len(self.shuffled_deck):
    #             self.card_display()
    #         else:
    #             self.listener.stop() 
    #             print("Deck finished")
    #             Main()
            
    #     elif key == Key.left or key == Key.down:
    #         self.listener_active = True
    #         self.shuffled_deck.append(self.shuffled_deck[self.card_num])
    #         self.card_num += 1
    #         if self.card_num < len(self.shuffled_deck):
    #             self.card_display()
    #         else:
    #             self.listener.stop() 
    #             print("Deck finished")
    #             Main()
    #     else:
    #         print(" - Incorrect Key pressed. Try Again")



    def card_display(self):
        clear()
        current_card = self.shuffled_deck[self.card_num]
        print(f'''
        {current_card.deck_name}
        -------------------------------------             
        {self.card_num} / {len(self.shuffled_deck)} cards studied

        {current_card.front}

        -------------------------------------  
        ''')

        # print("Press spacebar to see answer")

        self.show_card()


        # self.listener = Listener(on_release=self.on_key_release)
        # with self.listener as self.listener:
        #     self.listener.join()

            
            
    def show_answer_and_options(self):
        clear()
        current_card = self.shuffled_deck[self.card_num]
        print(f'''
        {current_card.deck_name} 
        -------------------------------------             
        {self.card_num} / {len(self.shuffled_deck)} cards studied   

        {current_card.front}

        ------------------------------------- 
         
        {current_card.back}
                        
         
        [ Wrong ] [ Need Review ] [ Easy ]

          [ A ]       [ S ]        [ D ]
        -------------------------------------  
        ''')

        self.progress_deck()



