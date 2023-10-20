import modules
import data

# modules.Main()

# modules.create_deck_from_file()

# print(modules.decks)

# modules.study_menu(modules.decks)


def  main_run(deck):

    formatted_card_bank = []

    for k,v in deck.items():
        deck_name = k
        for card in v:
            card_front = card["content"]
            card_back = card["answer"]
            total_card_num = card["tot_daily_deck_count"]
            new_card = modules.Card(card_front, card_back, total_card_num, deck_name)
            formatted_card_bank.append(new_card)

        study_deck = modules.Study(formatted_card_bank)
        study_deck.card_display()
     
    
main_run(data.deck1)








