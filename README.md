# T1A3 Terminal Application - FlashCard Application
## Adam Hutt 
## Student Number - 14793

[Github Repository](https://github.com/huttadam/Terminal-App-T1_A3-AdamHutt)

[My Trello Board](https://trello.com/b/klaHSd9M/terminal-application-coder-aca)

### Purpose of Application
The purpose of this application is to be a customisable flashcard, study application . Physical cards can be
be quite troublesome as they can take up a lot of time and space for the user. Creating, managaing and organizing the physical cards is a process that can be automated and made simple digitally. This application aims to make this process simpler and easier. In terms of customization , many people need to study many different things , so the features to create decks and cards helps serve its primary purpose.


#### Feature 1: Study a deck
This is the primary purpose and feature of this application. From the menu , the user selects a deck of cards to study and receives these cards in random order. The user only sees the front side of the card and has to recall the other side of the card. Once the user thinks they have the answer, they flip the card to reveal the answer. Based on the users guess and the answer, they then determine whether they need to see this car again in the study session. The user has 3 options to choose. The first option is their assumption was wrong , so this card should be showed two more times  randomly in the study session. The second option is 1 more repeat of the card, meaning the user got this answer but took a long time to time think of the answer or maybe the answer was close. Lastly, the third option is the answer was easy and the user doesnt need to see the card again. Anyone of these options will also progress to the next card in the deck. Once the user cycles through all the cards, the deck is complete.


#### Feature 2: Create a deck with a .txt file / Create a Deck Manually
The decks and cards need to be customizable, as peoples subject of study can be diffrent. This feature facilitates this solution and offers the user some options on how to create a deck. 
The most efficient way to create a deck is through the use of a .txt file. The user writes the front and back of their wanted card on a txt file line, seperating the front and back with a "/" symbol. The next line in the txt file would be another card. For some topics (foreign language/ Translation) it is useful to have the front and back reversed. The user has this option whether to let each line have two cards with the front and back reversed. From this specific formatting the file can be uploaded from the computer, named by the user and then generated into a deck for the user to study through. 
Another method is to create a deck manually. The user selects the option to create a deck manually. The user than names the deck and similarly to creating with a txt file, the deck will be saved in a JSON file and available for multiple sessions. However when created manually, it only creates a deck and no cards, so cards will needed to be added prior to studying.


#### Feature 3: Add Cards to a deck 
This feature enables the user to add more cards to a specific deck. After a lot of use the user would most likely rememeber all the answers to the cards and is able to add more to learn more on the topic. So the user can manually select the deck and add more cards to the deck. The user is prompted to input the front and back of the card and offered if they would to to generate another card but with the front and back reveresed also. This can be done for previously created decks from .txt file or a new manually created deck.


#### Feature 4: Change name of deck 
After some time the user may start to learn more and more on the topic and add additional cards with information that may not match the deck name anymore. For example, you may start your deck with "Japanese Greetings" but as more cards are added, more complex grammar structures cards have been added and doesnt fit the title any longer. For this the user can select the deck and change it. In our previous example maybe somehting like "Japanese Grammar" or something. The application will also not allow the same name for two decks to be used.


#### Feature 5: Delete a deck /Delete cards from a deck
Errors when creating can be common place or perhaps the information on a card is incorrect. These features from the Edit Menu , allow the user to delete a whole deck or more practically, delete specific cards in the deck. The application provides a list of the decks / cards in the deck to delete and the user simply selects and removes it from the deck or the deck is removed entirely.


### Testing

I automated parts of my test but still required some input to be entered manually. I have kept the code in the test.py tab and provided manual feedback for my features and application below. I have also attached the .txt files for testing in the docs file of the project.


| Test Method | Feature | Test |Expected Result| Actual Result |
|---|---|---|---|---|
| Manual              | Feature 1 - Study a Deck (Case 1)           | Cycle through the cards and test all possible inputs ('Z' = show card, 'A' = Wrong, 'S' = Need review, 'D' = Easy) | To perform based on their coding, repeat the cards if necessary and always and advance to the next card. | As expected |
| Manual              | Feature 1 - Study a Deck (Case 2)           | Receiving incorrect user input from the user, other than previously defined input. | To reset the current card and not advance or crash. | As expected |
| Half Automated      | Feature 2 - Create a Deck through user input .txt file (Case 1) | If an incorrectly formatted .txt file (test1.template.txt) is uploaded | To return to the main menu with a message informing the user and asking the user to check and correct the formatted file | As expected |
| Half Automated      | Feature 2 - Create a Deck through user input .txt file (Case 2) | Receiving a correctly formatted txt file (test2_template.txt) and runs through other requested inputs function correctly like "Would you like a reversed copy of card" or "Please enter name" | To upload into the Json file and immediately become a deck available to study. | As expected |




<!-- Test Method | Feature | Test | Expected result | Actual result 
--- | --- | --- | --- | ---
Manual | Feature 1 - Study a Deck (Case 1) |  Cycle through the cards and test all possible inputs ('Z' = show card, 'A' =  Wrong , 'S' = Need review, 'D' = Easy) | To perform based on their coding, repeat the cards if necessary and always and advance to next card. | As expected 

Manual | Feature 1 - Study a Deck (Case 2) | Receiving incorrect user input from the user, other than previously defined input.  | To reset the current card and not advance or crash. | As expected 

Half Automated | Feature 2 - Create a Deck through user input .txt file (Case 1) | If a incorrectly formatted .txt file (test1.template.txt) is uploaded  | To return to the main menu with a message informing the user and  asking the user to check and correct the formatted file | As expected 

Half automated | Feature 2 - Create a Deck through user input .txt file  (Case 2) | Recieving correctly formatted txt file (test2_template.txt) and runs through other requested inputs function correctly like "Would you like to a reversed copy of card" or "Please enter name"  | To upload into the Json file and immediately become a deck available to study. | As expected  --> 


### Implementation Plan

I found using the implementation plan on Trello very useful and a productive way to track my progress throughout the project. Although having to slightly change some ideas and adding additional/changing some features based on timing was a lot more stress-free as I could track the other work that needed to be done and manage my time.

Progress photos:

![Trello 1](/docs/Trello/D1-1.png)
![Trello 2](/docs/Trello/D2-2.png)
![Trello 3](/docs/Trello/D3%20-1.png)
![Trello 4](/docs/Trello/D4-1.png)
![Trello 5](/docs/Trello/D5%20-1.png)
![Trello 6](/docs/Trello/D6-1.png)
![Trello 7](/docs/Trello/D7-1.png)
![Trello 8](/docs/Trello/D8-1.png)
![Trello 9](/docs/Trello/completed.png)


Completed Features Checklists (Daily checklist photos also in docs file):

![Trello 1](/docs/Trello/D10-2.png)
![Trello 2](/docs/Trello/D10-4.png)
![Trello 3](/docs/Trello/D10-5.png)


### Style Guide
* Adhered to the PEP8 styling guidelines as closely as possible.
* Some cases for example, like the logo or f string infomration could not be wrapped to under 79 spaces.
* Spacing between lines are one spaced or two depending on function or class.
* Naming conventions followed, Capitals used for Classes and snake case for variable/fucntions.


### How to import

Step 1:
Please ensure you are inside the src file of the terminal project folder. (cd AdamHutt_T1A3/src) 

Step 2:
Run the below into the command line
```bash
bash flashcard.sh
```
If Python is not installed, you will recieve a message to download or you can download here. [Python](https://www.python.org/downloads/release/python-3107/)

Alternatively ..

Step 1:
Ensure that Git and Python are installed on your computer. Git info available here [Git](https://github.com/git-guides/install-git)

Step 2:
Please run the below in your desired directory command line.
```bash
cd Terminal-App-T1_A3-AdamHutt/src
```
Step 3:
Run the below into the command line
```bash
bash flashcard.sh
```

Bash code example below
```bash
#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
    echo 'Python3 not downlaoded , Please dowload to run.' >&2
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py $1
deactivate
```

### Imported Packages (requirements,dependencies on requirements.txt)

* sys
* os
* random
* json
* clear
* colorama


### References
