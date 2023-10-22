import json

decks_data = [
        {"Korean Example Deck":
        [{'content': 'Hello', 'answer': '안녕하세요 (annyeonghaseyo)'},
        {'content': '안녕하세요 (annyeonghaseyo)', 'answer': 'Hello'}]},
        
        {'Basic Japanese':[
        {'content': 'Hello', 'answer': 'こんにちは (Konnichiwa)'},
        {'content': 'Good morning', 'answer': 'おはよう (Ohayou)'},
        {'content': 'Good night', 'answer': 'おやすみなさい (Oyasuminasai)'},
        {'content': 'Thank you', 'answer': 'ありがとう (Arigatou)'},
        {'content': "You're welcome", 'answer': 'どういたしまして (Douitashimashite)'},
        {'content': 'Please', 'answer': 'お願いします (Onegaishimasu)'},
        {'content': 'Excuse me', 'answer': 'すみません (Sumimasen)'},
        {'content': "I'm sorry", 'answer': 'ごめんなさい (Gomen nasai)'},
        {'content': 'How are you?', 'answer': 'お元気ですか？ (Ogenki desu ka?)'},
        {'content': "What's your name?", 'answer': 'お名前は何ですか？ (Onamae wa nan desu ka?)'},
        {'content': 'こんにちは (Konnichiwa)', 'answer': 'Hello'}, 
        {'content': 'おはよう (Ohayou)', 'answer': 'Good morning'},
        {'content': 'おやすみなさい (Oyasuminasai)', 'answer': 'Good night'},
        {'content': 'ありがとう (Arigatou)', 'answer': 'Thank you'},
        {'content': 'どういたしまして (Douitashimashite)', 'answer': "You're welcome"},
        {'content': 'お願いします (Onegaishimasu)', 'answer': 'Please'},
        {'content': 'すみません (Sumimasen)', 'answer': 'Excuse me'},
        {'content': 'ごめんなさい (Gomen nasai)', 'answer': "I'm sorry"},
        {'content': 'お元気ですか？ (Ogenki desu ka?)', 'answer': 'How are you?'},
        {'content': 'お名前は何ですか？ (Onamae wa nan desu ka?)', 'answer': "What's your name?"}]
        }

]


with open('decks.json', 'w') as file:
    json.dump(decks_data, file, indent=2)


