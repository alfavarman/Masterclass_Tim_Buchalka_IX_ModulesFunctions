import tkinter, random


def load_cards(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    # # Tkinter ver below 8.6 doesnt read png
    # if tkinter.TkVersion >= 8.6
    #     extension = 'png'
    # else:
    #     extension = 'ppm'

    # append suites to card_images
    for suit in suits:
        for card in range(1, 11):
            # card_n = f'{card:02d}' IF file name has 0 in front
            name = f'cards_png/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, name))

        for card in face_cards:
            name = f'cards_png/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, name))


def deal_card(frame):
    # pop the next card of the top of the deck
    next_card = deck.pop(0)
    # add an image to an label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return card face value
    return next_card


def deal_dealer():
    deal_card(frameDealer_cards)


def deal_player():
    deal_card(framePlayer_cards)


# open and set up window
mainWindow = tkinter.Tk()
mainWindow.title('BlackJack')
mainWindow.geometry('800x600')

# Text -> Variable 'May the best win!' -> 'Dealer/Player Wins! Congratulations!'
# result_text = tkinter.StringVar
labelResult = tkinter.Label(mainWindow, text="May the best Win!", fg='blue')
labelResult.grid(row=0, column=0, columnspan=6)

# frame for table
frameTable = tkinter.Frame(mainWindow, relief='sunken', background='green')
frameTable.grid(row=1, column=0, rowspan=2, columnspan=5, sticky='nsew')

# Dealer'
# frame for dealer label and points
frameDealer = tkinter.Frame(frameTable, background='green')
frameDealer.grid(row=0, column=0)

# frame for dealer_cards
frameDealer_cards = tkinter.Frame(frameTable, background='green')
frameDealer_cards.grid(row=0, column=1, columnspan=4)

# label for dealer
labelDealer = tkinter.Label(frameDealer, text='Dealer', fg='white', background='green')
labelDealer.grid(row=0, column=0, sticky='new')

# label for dealer points
labelDealer_Points = tkinter.IntVar()
tkinter.Label(frameDealer, text='Dealer', fg='white', background='green').grid(row=0, column=0)
tkinter.Label(frameDealer, textvariable=labelDealer_Points, fg='white', background='green').grid(row=1, column=0)

# Player'
# frame for player label and points
framePlayer = tkinter.Frame(frameTable, background='green')
framePlayer.grid(row=1, column=0)

# frame for player_cards
framePlayer_cards = tkinter.Frame(frameTable, background='green')
framePlayer_cards.grid(row=1, column=1, columnspan=4, sticky='we')

# label for player
labelPlayer = tkinter.Label(framePlayer, text='Player', fg='white', background='green')
labelPlayer.grid(row=0, column=0, sticky='new')

# label for player points
labelPlayer_Points = tkinter.IntVar()
tkinter.Label(framePlayer, text='Player', fg='white', background='green').grid(row=0, column=0)
tkinter.Label(framePlayer, textvariable=labelPlayer_Points, fg='white', background='green').grid(row=1, column=0)

# frame for buttons:
frameButtons = tkinter.Frame(mainWindow)
frameButtons.grid(row=3, column=0)

# Dealer Button
buttonDealer = tkinter.Button(frameButtons, text='Dealer', relief='raised', borderwidth=2, command=deal_dealer)
buttonDealer.grid(row=0, column=0)
# Player Button
buttonPlayer = tkinter.Button(frameButtons, text='Player', relief='raised', borderwidth=2, command=deal_player)
buttonPlayer.grid(row=0, column=1)

# decks
deck = []
load_cards(deck)
random.shuffle(deck)

# dealer/player hands:
deal_hand = []
player_hand = []

mainWindow.mainloop()
