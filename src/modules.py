from clear import clear # installed  clear
import os
from pynput.keyboard import Key, Listener
import random
import json


# ///////////////// Navigation / Menu's /////////////////


def get_lines_from_file(file_path):
    try: 
        while True:
            if os.path.isfile(file_path):
                with open(file_path, 'r') as c:
                    return c.readlines()
            else:
                print("There was a problem reading , Please check and enter again.")
                create_deck_from_file()
                break
    
    except ValueError:
        print("Please reformat the text must be - front, back - and another card on a new line ")




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
        self.instructions =("Please choose from the list of options below\n")
        self.options = '''

        [ 1 ] = Study a Deck

        [ 2 ] = Create a Deck / Add Cards

        [ 3 ] = Edit Deck

        [ 4 ] = Exit the app


        '''


    def change_screen(self):
        clear()
        print(self.logo)
        print(self.instructions)
        

    
    def display_available_decks(self):
        with open('decks.json', 'r') as json_file:
            self.x = json.load(json_file)

        self.ava_deck_names = []
        for card_name_deck in self.x:
            for key in card_name_deck.keys():
                self.ava_deck_names.append(key)


        print("Available Decks:\n")
        for i, key in enumerate(self.ava_deck_names, start=1):
            print(f"[ {i} ] {key}\n")
        


class Main(MenuLogo):
    def __init__(self):
        super().__init__()

        self.change_screen()

        print(self.options)
   

        while True:
            # try:
            user_main_choice = int(input("Please choose your option with the number and hit enter: "))
            if user_main_choice == 1:
                StudyMenu()
                break
            elif user_main_choice == 2:
                DeckCreator()
                break
            elif user_main_choice == 3:
                pass
            elif user_main_choice == 4:
                pass
            else:
                print("Invalid Input, please try again")
            
        # except ValueError:
        #     print("Please enter a number 1, 2, 3 or 4")
        #     continue






class StudyMenu(MenuLogo):
    def __init__(self):
        super().__init__()
        
        self.change_screen()


        self.display_available_decks()

        while True:
            # try:
            selected_index = int(input("\nPlease choose with the number and hit enter: "))
            if 1 <= selected_index <= len(self.ava_deck_names):
                selected_deck = self.x[selected_index - 1]
                CardFormatter.init_deck(selected_deck)
                
            else:
                print("Invalid choice. Please choose with the corresponding number.")
            
            # except ValueError:
            #     print("Please input a number")
            #     continue
    





# ///////////////// Create a Deck  /////////////////

class DeckCreator(MenuLogo):
        
    def __init__(self):
        super().__init__()

        self.change_screen()

        print('''

        [ 1 ] = Create a deck with .txt file 

        [ 2 ] = Create a new deck

        [ 3 ] = Create a Card and add to deck

        [ 4 ] = Main Menu
        ''')

        
        # try:
        create_menu_choice = int(input("Please choose with the number and hit enter: "))
        if create_menu_choice == 1:
            self.change_screen()
            push_deck_to_Json(create_deck_from_file())
            
                    
        elif create_menu_choice == 2:
            self.change_screen()
            push_deck_to_Json([{}])

        elif create_menu_choice == 3:
            self.change_screen()
            self.create_and_add_card()

        elif create_menu_choice == 4:
            clear()
            pass
        
        else:
            print("Invalid Input, please try again")

        # except ValueError:
        #     print("Incorrect input, try again")
        
        # except TypeError:
        #     print("Incorrect input, try again")


        # while True:

        #     new_name = input("What do you want to name the deck?: ")
        #     if push_deck_to_Json(new_name):
        #         break
        #     else:
        #         print("This deck already exists, please enter another \n")



        print('''

        [ 1 ] = Study decks
              
        [ 2 ] = Add Cards to deck

        [ 3 ] = Main Menu

        ''') 

        post_create_option = int(input("Please choose with the number and hit enter:"))


        if post_create_option == 1:
            StudyMenu()
        elif post_create_option == 2:
            pass

        elif post_create_option == 3:
            Main()

    def create_and_add_card(self):
        self.display_available_decks()
        while True:
            create_add_choice = int(input("\nPlease choose with the number and hit enter: "))
            if 1 <= create_add_choice <= len(self.ava_deck_names):
                selected_deck = self.x[create_add_choice - 1]
                for val in selected_deck.values():
                    add_card_fro = input("Please write your main content (front): ")
                    add_card_back = input("Please write your answer (back): ")
                    new_card_1 = create_and_reverse(add_card_fro, add_card_back)
                    new_card_2 = create_and_reverse(add_card_back, add_card_fro)
                    selected_deck.update(new_card_1)
                    selected_deck.update(new_card_2)

                    with open('decks.json', 'w') as json_file:
                        json.dump(selected_deck, json_file, indent=2)

            else:
                print("Invalid choice. Please choose with the corresponding number.")




def create_and_reverse(content,answer):
    card_info ={
        "content":content,
        "answer": answer
    }
    return card_info


def create_deck_from_file():
    
    new_deck =[]

    file_path = input("Enter the path or name of the text file: ")

    lines_from_file = get_lines_from_file(file_path)
    try:
        for line in lines_from_file:
            content, answer = line.strip().split('/')
            new_deck.append(create_and_reverse(content,answer))
            new_deck.append(create_and_reverse(answer,content))
    
    except ValueError:
        print("formatting error, please check .txt file and ensure only / ")
        create_deck_from_file()

    return new_deck


def push_deck_to_Json(deck_cards):
    
    while True:
        name_input = input("What do you want to call your deck?: ")
        with open('decks.json', 'r') as json_file:
            d = json.load(json_file)

        name_exists = False
        for deck in d:
            for key in deck.keys():
                if name_input in deck.keys():
                    name_exists = True
                    break

        if not name_exists:
            template_created_dict = {name_input: deck_cards}
            d.append(template_created_dict)

            with open('decks.json', 'w') as json_file:
                json.dump(d, json_file, indent=2)

            print(f"Deck '{name_input}' has been created.\n")
            break
        else:
            print("This deck name already exists. Please enter another.\n")










# while True:
#     new_name = input("What do you want to name the deck?: ")
#     if push_deck_to_Json(new_name,create_deck_from_file()):
#         break
#     else:
#         print("This deck already exists, please enter another \n")



#     print('''

#     [ 1 ] = Study decks 

#     [ 2 ] = Main Menu

#     ''') 

#     post_create_option = int(input("Please choose with the number and hit enter:"))


#     if post_create_option == 1:
#         StudyMenu()
#     elif post_create_option == 2:
#         Main()


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
        print("type Q to exit")

        if self.next_card == 'A' or self.next_card == 'S':
            self.shuffled_deck.append(self.shuffled_deck[self.card_num])
            self.card_num += 1
            self.card_display()
        elif self.next_card == 'Q':
            Main()
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

