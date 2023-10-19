study_deck_template = [1, "Deck Name", 30 , 14] # number , Name, total cards in deck, Daily cards to learn


# Is going to be the deck name
single_card_template = [
                        {"card_num": 0, # card number (unique)
                         "tot_daily_deck_count": 0, # out of total cards to learn from today
                         "content": "lorem", # content / Question
                         "answer": "lorem", # Answer
                         }
                        ]


def create_deck_from_file():
    deck_name =[]

    # Open the file for reading
    with open("src/template.txt", 'r') as c:
        lines = c.readlines()

    for index,line in enumerate(lines):
        content, answer = line.strip().split(', ')
        index += 1
        card_info = {
            "card_num": index * 2,  # card number (unique)
            "tot_daily_deck_count": len(lines) * 2,  # out of the total cards to learn from today
            "content": content,  # content / Question
            "answer": answer,  # Answer
        }
        deck_name.append(card_info)

    print(deck_name)

    # deck_name = input("what do you want to name the deck?: ")

create_deck_from_file()

