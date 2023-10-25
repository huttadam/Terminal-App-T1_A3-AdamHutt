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


 # def show_card(self):
    #     self.show_card_input = input(yel_text +"Press 'Z' and enter to show: ")

    #     if self.show_card_input.upper() == 'Z':
    #         self.show_answer_and_options()


    # def progress_deck(self):
    #     print("type Q to exit")
    #     self.next_card = input(yel_text +"Press 'A' 'S' or 'D': ")
        

    #     if self.next_card.upper() == 'A' or self.next_card.upper() == 'S':
    #         self.shuffled_deck.append(self.shuffled_deck[self.card_num])
    #         self.card_num += 1
    #         self.card_display()
    #     elif self.next_card.upper() == 'Q':
    #         Main()
    #     elif self.next_card.upper() == 'D':
    #         self.card_num += 1
    #         self.card_display()


    # def card_display(self):
    #     clear()
    #     current_card = self.shuffled_deck[self.card_num]
    #     print(f'''
    #     {current_card.deck_name}
    #     -------------------------------------             
    #     {self.card_num} / {len(self.shuffled_deck)} cards studied

    #     {current_card.front}

    #     -------------------------------------  
    #     ''')


    #     self.show_card()

    #     # self.listener = Listener(on_release=self.on_key_release)
    #     # with self.listener as self.listener:
    #     #     self.listener.join()
      
    # def show_answer_and_options(self):
    #     clear()
    #     current_card = self.shuffled_deck[self.card_num]
    #     print(f'''
    #     {current_card.deck_name} 
    #     -------------------------------------             
    #     {self.card_num} / {len(self.shuffled_deck)} cards studied   

    #     {current_card.front}

    #     ------------------------------------- 
         
    #     {current_card.back}
                        
         
    #     [ Wrong ] [ Need Review ] [ Easy ]

    #       [ A ]       [ S ]        [ D ]
    #     -------------------------------------  
    #     ''')

    #     self.progress_deck()