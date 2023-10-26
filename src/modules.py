import sys
import os
import random
import json
from clear import clear
from colorama import Fore, Style, init
import time
init(autoreset=True)

# ///////////////// Navigation / Menu's /////////////////


class MenuLogo():
    def __init__(self):
        self.logo = '''
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

        self.greeting = "Welcome to the Flash Card App , customize your study"
        "and start now ! \n"
        self.instructions = ("Please choose from the list of options below\n")
        self.options = '''

        [ 1 ] = Study a Deck

        [ 2 ] = Create a Deck / Add Cards

        [ 3 ] = Edit Deck

        [ 4 ] = Exit the app

        '''

        self.y_text = Fore.YELLOW
        self.c_text = Fore.CYAN
        self.b_text = Style.BRIGHT

    def post_function_options(self,message_for_user):
        self.change_screen_to_menu()

        print(self.c_text + f"{message_for_user}\n")

        print(self.options)
        try:
            while True:
                post_create_option = int(input(self.y_text + "Please choose with "
                                               "the number and hit enter: "))
                if post_create_option == 1:
                    StudyMenu()
                elif post_create_option == 2:
                    CreateDeckMenu()
                elif post_create_option == 3:
                    EditMenu()
                elif post_create_option == 4:
                    sys.exit()
                else:
                    print("Invalid Input, please try again")
        except ValueError:
            self.post_function_options("Invalid choice. Please choose using "
                                       "the numbers.")



    def change_screen_to_menu(self):
        clear()
        print(Fore.RED + self.b_text + self.logo)
        print(self.y_text + self.b_text + self.instructions)



    def display_available_decks(self):
        with open('decks.json', 'r') as json_file:
            self.x = json.load(json_file)

        self.ava_deck_names = []

        for card_name_deck in self.x:
            for self.single_deck in card_name_deck.keys():
                self.ava_deck_names.append(self.single_deck)

        if not self.ava_deck_names:
            self.post_function_options(self.c_text + "There are no decks available"
                                       " - please create one first") 
        else:
            print(self.y_text + "Available Decks:\n")
            for i, key in enumerate(self.ava_deck_names, start=1):
                print(f"[ {i} ] {key}\n")


class Main(MenuLogo):
    def __init__(self):
        super().__init__()

        self.change_screen_to_menu()

        print(self.options)
 
        while True:
            try:
                user_main_choice = int(input(self.y_text +"Please choose your "
                                             "option with the number and hit"
                                             " enter: "))
                if user_main_choice == 1:
                    StudyMenu()
                elif user_main_choice == 2:
                    CreateDeckMenu()
                elif user_main_choice == 3:
                    EditMenu()
                elif user_main_choice == 4:
                    sys.exit()
                else:
                    print("Invalid Input, please try again")
            
            except ValueError:
                print("Invalid choice. Please choose using the numbers.")
            except UnboundLocalError:
                self.post_function_options("Theres no cards in this deck.")

   
class StudyMenu(MenuLogo):
    def __init__(self):
        super().__init__()
        self.change_screen_to_menu()
        self.display_available_decks()

        selected_index = int(input(self.y_text +"\nPlease choose with the number" 
                                   "and hit enter: "))
        if 1 <= selected_index <= len(self.ava_deck_names):
            selected_deck = self.x[selected_index - 1]
            for sd_val in selected_deck.values():
                if sd_val == [{}]:
                    self.post_function_options(self.c_text + "That deck has no "
                                            "cards, please add cards to use")   
                else:
                    CardFormatter(selected_deck)     
        else:
            print("Invalid choice. Please choose using the numbers.")

# # ///////////////// Study Function  /////////////////

#Take infromation from the Json and formats to suite the function
class CardFormatter:
    def __init__(self,deck):

        formatted_card_bank = []

        for k,v in deck.items():
            deck_name = k
            for card in v:
                card_front = card["content"]
                card_back = card["answer"]
                new_card = Card(card_front, card_back, deck_name)
                formatted_card_bank.append(new_card)
            # this list is the info as objects
            study_deck = Study(formatted_card_bank)
            study_deck.run_deck()
            #run through the study function



class Card:
    '''makes an object with required information'''
    def __init__(self, front, back, deck_name):
        self.front = front
        self.back = back
        self.deck_name = deck_name


class Study(MenuLogo):
    '''receives list of obj to to be studied and hold'''
    def __init__(self, for_deck):
        super().__init__()
        self.for_deck = for_deck
        self.shuffled_deck = for_deck[:]
        random.shuffle(self.shuffled_deck)
        self.card_num = 0
        self.y_text = Fore.YELLOW
        self.c_text = Fore.CYAN

        # m_l_instance = MenuLogo()

        # m_l_instance.y_text = Fore.YELLOW
        # m_l_instance.c_text = Fore.CYAN


    def run_deck(self):
        ''' Runs formmated deck and allows user to repeat or pass'''
        # m_l_instance = MenuLogo()
        deck_len_ext = len(self.shuffled_deck)

        while self.card_num < deck_len_ext:
            current_card = self.shuffled_deck[self.card_num]
            clear()
            print(self.c_text +f'''
            {current_card.deck_name}
            -------------------------------------
            {self.card_num} / {len(self.shuffled_deck)} cards studied

            {current_card.front}

            -------------------------------------
            ''')
            show_card_input = input(self.y_text +"\nPress 'Z' to show"
                                    " the answer: ").lower()

            if show_card_input == 'z':
                clear()
                print(self.c_text + f'''
            {current_card.deck_name}
            -------------------------------------
            {self.card_num} / {len(self.shuffled_deck)} cards studied

            {current_card.front}

            -------------------------------------

            {current_card.back}

            [ Wrong ] [ Need Review ] [ Easy ]

              [ A ]        [ S ]       [ D ]
            -------------------------------------
                ''')

                next_card = input(self.y_text +"Press 'A' or 'S' to shuffle back"
                                  " in deck. 'D' to move to the next card."
                                  " 'Q' to exit: ").lower()

                if next_card == 'q':
                    m_l_instance.post_function_options("You quit the deck")
                elif next_card == 's':
                    self.shuffled_deck.append(self.shuffled_deck[self.card_num])
                    deck_len_ext += 1
                    self.card_num += 1
                elif next_card == 'a':
                    self.shuffled_deck.append(self.shuffled_deck[self.card_num])
                    self.shuffled_deck.append(self.shuffled_deck[self.card_num])
                    deck_len_ext += 2
                    self.card_num += 1
                elif next_card == 'd':
                    self.card_num += 1

            message =(self.c_text + f'''
            {current_card.deck_name}
            -------------------------------------
            {self.card_num} / {len(self.shuffled_deck)} - All cards in the deck!

            You repeated {self.card_num - len(self.for_deck)} cards

            Well done!, Deck Complete


            -------------------------------------
            ''' )
        self.post_function_options(message)  

# ///////////////// Create a Deck  /////////////////

class CreateDeckMenu(MenuLogo):
    '''Handles deck,card and creating handling'''
    def __init__(self):
        super().__init__()

        self.change_screen_to_menu()

        while True:
            self.change_screen_to_menu()

            try:
                print('''

        [ 1 ] = Create a deck with .txt file 

        [ 2 ] = Create a new deck

        [ 3 ] = Create a Card and add to deck

        [ 4 ] = Main Menu
                ''')

                create_menu_choice = int(input(self.y_text +"Please choose with "
                                               "the number and hit enter: "))

                if create_menu_choice == 1:
                    self.change_screen_to_menu()
                    self.push_deck_to_json(self.create_deck_from_file())

                elif create_menu_choice == 2:
                    self.change_screen_to_menu()
                    self.push_deck_to_json([])

                elif create_menu_choice == 3:
                    self.change_screen_to_menu()
                    self.create_and_add_card()

                elif create_menu_choice == 4:
                    self.post_function_options("")

            except ValueError:
                print("Invalid choice. Please choose using the numbers.")


    def create_and_add_card(self):
        self.display_available_decks()
        while True:
            create_add_choice = int(input(self.y_text +"\nPlease choose with the "
                                          "number and hit enter : "))
            if 1 <= create_add_choice <= len(self.ava_deck_names):
                selected_deck = self.x[create_add_choice - 1]
                for key in selected_deck.keys():
                    add_card_fro = input(self.c_text +"\nPlease write your main "
                                         "content (front): ")
                    add_card_back = input(self.c_text +"\nPlease write your "
                                          "answer (back): ")
                    want_double = input(self.c_text +"\n Do you want two cards"
                                        ", reveresed, front and back (Y/N)?")
                    
                    if want_double.lower() == "n":
                        new_card1 = self.create_and_reverse(add_card_fro, add_card_back)
                        selected_deck[key].append(new_card1)
                    elif want_double.lower() == "y":
                        new_card1 = self.create_and_reverse(add_card_fro, add_card_back)
                        new_card2 = self.create_and_reverse(add_card_back, add_card_fro)
                        selected_deck[key].append(new_card1)
                        selected_deck[key].append(new_card2)
                    
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")

                    with open('decks.json', 'w') as json_file:
                        json.dump(self.x, json_file, indent=2)

                    print(f"\nCards successfully created added to {key}\n")

                    while True:
                        add_another_card = input(self.y_text + (f"Would you like to add another card to {key}? (Y/N)? "))
                        if add_another_card.lower() == 'y':
                            self.create_and_add_card()
                        elif add_another_card.lower() == 'n':
                            self.post_function_options("Card creating finished")
                        else:
                            print("Invalid input. Please enter 'Y' or 'N'.")
            else:
                print("Invalid choice. Please choose with the "
                      "corresponding number.")

    def get_lines_from_file(self,file_path):
        try:
            while True:
                if os.path.isfile(file_path):
                    with open(file_path, 'r') as c:
                        return c.readlines()
                else:
                    self.post_function_options("Invalid file address , Please"
                                               " check and enter again.")

        except ValueError:
            print("Please reformat the text file must be - 'front / back'"
                  " - and another card on a new line ")

    def create_and_reverse(self,content,answer):
        card_info ={
            "content":content,
            "answer": answer
            }
        return card_info


    def create_deck_from_file(self):
        new_deck =[]
        file_path = input(self.y_text +"Enter the path or name of the text file: ")
        lines_from_file = self.get_lines_from_file(file_path)
        try:
            txt_inp_swap = input("\n Do you want get 2 for each side, "
            "2-sided Y /N ? ")
            
            for line in lines_from_file:
                content, answer = line.strip().split('/')
                
                if txt_inp_swap.lower() == "y":
                    new_deck.append(self.create_and_reverse(content, answer))
                    new_deck.append(self.create_and_reverse(answer, content))
                elif txt_inp_swap.lower() == "n":
                    new_deck.append(self.create_and_reverse(content, answer))
                else:
                    ("Invalid input. Please enter 'Y' or 'N'.")


        except ValueError:
            self.post_function_options("Formatting error, please check .txt "
                                       "file and ensure  '/' used once in"
                                       " a line to seperate ")
        except TypeError:
            self.post_function_options("Please ensure file is .txt")

        return new_deck


    def push_deck_to_json(self,deck_cards):
        while True:
            name_input = input(self.y_text +"\nWhat do you want to call"
                               " your deck?: ")
            with open('decks.json', 'r') as json_file:
                d = json.load(json_file)

            name_exists = False
            for deck in d:
                if name_input in deck.keys():
                    name_exists = True
                    break

            if not name_exists:
                template_created_dict = {name_input: deck_cards}
                d.append(template_created_dict)

                with open('decks.json', 'w') as json_file:
                    json.dump(d, json_file, indent=2)

                self.post_function_options(f"Deck '{name_input}' has"
                                           " been created.\n")
                break
            else:
                print("\nThis name already exists. Please enter another\n")

# ///////////////// Edit Menu /////////////
class EditMenu(MenuLogo):
    '''handles editing functions'''
    def __init__(self):
        super().__init__()

        self.change_screen_to_menu()

        print('''

        [ 1 ] = Change Name of deck 

        [ 2 ] = Delete a Card in a deck

        [ 3 ] = Delete Deck
              
        [ 4 ] = Return to Main Menu

        ''')

        while True:
            try:
                edit_menu_choice = int(input(self.y_text +"Please choose with "
                                             "the number and hit enter:"))

                if edit_menu_choice == 1:
                    self.change_screen_to_menu()
                    print("Which name would you like to change? \n")
                    self.display_available_decks()
                    self.edit_name_of_deck()

                elif edit_menu_choice == 2:
                    self.change_screen_to_menu()
                    print("Which deck is the card you would you like to"
                          " change? \n")
                    self.display_available_decks()
                    self.delete_card_in_deck()

                elif edit_menu_choice == 3:
                    self.change_screen_to_menu()
                    print("Which deck would you like to delete? \n")
                    self.display_available_decks()
                    self.delete_deck()

                elif edit_menu_choice == 4:
                    self.post_function_options("")

            except ValueError:
                print("Invalid choice. Please choose using the numbers.")


    def edit_name_of_deck(self):
        while True:
            try:
                edit_name_choice = int(input(self.y_text +"\nPlease choose the "
                                             "deck to rename by its number "
                                             "and hit enter: "))
                if 1 <= edit_name_choice <= len(self.ava_deck_names):
                    selected_deck = self.x[edit_name_choice - 1]
                    old_deck_name = self.ava_deck_names[edit_name_choice - 1]

                    while True:
                        new_deck_name = input(self.y_text +f"\nPlease enter a new name for the deck : '{old_deck_name}': ")

                        name_exists = False
                        for deck in self.x:
                            if new_deck_name in deck:
                                name_exists = True
                                break

                        if not name_exists:
                            selected_deck[new_deck_name] = selected_deck.pop(old_deck_name)
                            with open('decks.json', 'w') as json_file:
                                json.dump(self.x, json_file, indent=2)
                            self.post_function_options(f"Deck name changed to : '{new_deck_name}'.\n")
                            break
                        else:
                            print("This deck name already exists. Please enter"
                                  " another.\n")

                    break
            except ValueError:
                print("Invalid choice. Please choose using the numbers")


    def delete_card_in_deck(self):
        while True:
            try:
                del_card_deck_choice = int(input(self.y_text + "\nPlease choose "
                                                 "the deck the card contains:"
                                                 " "))
                if 1 <= del_card_deck_choice <= len(self.ava_deck_names):
                    selected_deck = self.x[del_card_deck_choice - 1]
                    for key, value in selected_deck.items():
                        if not value:
                            self.post_function_options("There are no cards "
                                                       "in that deck")
                            break

                        self.change_screen_to_menu()
                        print(f"Cards in deck: {key}\n")
                        for i, deck in enumerate(value, start=1):
                            print(f"[ {i} ]: {deck}\n")

                        edit_c_number = int(input(self.y_text + "\nWhat number ca"
                                                  "rd would you like to "
                                                  "delete? "))
                        if edit_c_number == 0:
                            break

                        if 1 <= edit_c_number <= len(value):
                            deleted_card = value.pop(edit_c_number - 1)  
                            with open('decks.json', 'w') as json_file:
                                json.dump(self.x, json_file, indent=2)
                            self.post_function_options(f"Card {edit_c_number}: {deleted_card} deleted successfully from '{key}'\n")
                        else:
                            print("Invalid card number. Please enter a valid "
                                  "number.")

                    break
                else:
                    print("Invalid deck choice. Please enter a valid deck"
                          " number.")
            except ValueError:
                print("Invalid input. Please enter a number")


    def delete_deck(self):
        while True:
            del_card_choice = int(input(self.y_text +"\nPlease choose the deck "
                                        "to delete: "))
            if 1 <= del_card_choice <= len(self.ava_deck_names):
                selected_deck = self.x[del_card_choice - 1]
                self.x.remove(selected_deck)

                with open('decks.json', 'w') as json_file:
                    json.dump(self.x, json_file, indent=2)
                break

        self.post_function_options(f" '{self.single_deck}' was successfully"
                                    " deleted")