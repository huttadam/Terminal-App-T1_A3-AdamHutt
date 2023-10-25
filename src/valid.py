# class Study:
#     def __init__(self, for_deck):
#         self.for_deck = for_deck
#         self.card_num = 0
#         self.shuffled_deck = for_deck[:] 
#         random.shuffle(self.shuffled_deck)
#         self.show_answer = False
#         self.repeat_card = False
#         self.finished = False

#     def on_key_release(self, key):
#         if key == Key.esc:
#             self.finished = True
#         elif key == Key.space:
#             self.show_answer = True
#         elif key == Key.left or key == Key.down:
#             self.repeat_card = True
#         elif key == Key.right:
#             self.card_num += 1

#     def run_deck(self):
#         m_l_instance = MenuLogo()
#         deck_len_ext = len(self.shuffled_deck)
#         self.card_num = 0

#         listener = keyboard.Listener(on_release=self.on_key_release)
#         listener.start()

#         while self.card_num < deck_len_ext:
#             current_card = self.shuffled_deck[self.card_num]
#             clear()  # Clear the terminal at the beginning
#             print(cya_text + f'''
#             {current_card.deck_name}
#             -------------------------------------
#             {self.card_num} / {len(self.shuffled_deck)} cards studied

#             {current_card.front}

#             -------------------------------------
#             ''')
#             print(yel_text + "Press Space bar to see result")
            
#             if self.show_answer:
#                 clear()  # Clear the terminal only when showing the answer
#                 print(cya_text + f'''
#                 {current_card.deck_name}
#                 -------------------------------------
#                 {self.card_num} / {len(self.shuffled_deck)} cards studied

#                 {current_card.front}

#                 -------------------------------------

#                 {current_card.back}

#                 [ Wrong ] [ Need Review ] [ Easy ]

#                 [ A ]       [ S ]        [ D ]
#                 -------------------------------------
#                 ''')
#                 self.show_answer = False  # Reset the flag after showing the answer
#                 print(yel_text + "Press '<' or 'v' to shuffle back in the deck. '>' to move to the next card. 'esc' to exit: ")

#         listener.stop()  # Stop the keyboard listener

#         message = (cya_text + f'''
#             {current_card.deck_name}
#             -------------------------------------
#             {self.card_num} / {len(self.shuffled_deck)} - All cards in the deck!

#             You repeated {self.card_num - len(self.for_deck)} cards

#             Well done!, Deck Complete

#             -------------------------------------
#             ''' )
#         m_l_instance.post_function_options(message)