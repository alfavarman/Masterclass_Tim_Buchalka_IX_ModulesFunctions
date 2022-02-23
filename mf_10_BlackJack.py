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
            # append 10, image bc all face cards are count as 10
            # (()) bc append can take one value
            card_images.append((10, image))


def deal_card(frame):
    # pop the next card of the top of the deck
    next_card = deck.pop(0)
    # add an image to an label and display the label
    label = tkinter.Label(frame, image=next_card[1], relief='raised')
    label.image_reference = next_card[1]
    label.pack(side='left')
    # return card face value
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list
    # only one ace can have value 11, and this will be reduce to 1 if hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_hand.append(deal_card(frameDealer_cards))
    dealer_score = score_hand(dealer_hand)
    labelDealer_Points.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set('Dealer wins!')
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set('Player wins!')
    elif dealer_score > player_score:
        result_text.set('Dealer wins!')
    else:
        result_text.set('Draw!')
    # global dealer_ace
    # global dealer_score
    # card_value = deal_card(frameDealer_cards)[0]
    # if card_value == 1 and not dealer_ace:
    #     card_value = 11
    # dealer_score += card_value
    # # if player is Bust use Ace score as 1
    # if dealer_score > 21 and dealer_ace:
    #     dealer_score -= 10
    # labelDealer_Points.set(dealer_score)
    # if dealer_score > 21:
    #     result_text.set('Player Wins')


def deal_player():
    player_hand.append(deal_card(framePlayer_cards))
    player_score = score_hand(player_hand)

    labelPlayer_Points.set(player_score)
    if player_score > 21:
        result_text.set('Dealer Wins!')
    # global player_ace
    # global player_score
    # card_value = deal_card(framePlayer_cards)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += int(card_value)
    # # if player is Bust use Ace score as 1
    # if int(player_score) > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # labelPlayer_Points.set(player_score)
    # if int(player_score) > 21:
    #     result_text.set('Dealer Wins')


# open and set up window
mainWindow = tkinter.Tk()
mainWindow.title('BlackJack')
mainWindow.geometry('800x600')

# Text -> Variable 'May the best win!' -> 'Dealer/Player Wins! Congratulations!'
result_text = tkinter.StringVar()
result_text.set("May the best Win!")
labelResult = tkinter.Label(mainWindow, textvariable=result_text, fg='blue')
labelResult.grid(row=0, column=0, columnspan=6)

# frame for table
frameTable = tkinter.Frame(mainWindow,  relief='sunken', background='green')
frameTable.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Dealer'
# frame for dealer label and points
frameDealer = tkinter.Frame(frameTable, background='green')
frameDealer.grid(row=0, column=0)

# frame for dealer_cards
frameDealer_cards = tkinter.Frame(frameTable, background='green')
frameDealer_cards.grid(row=0, column=1, sticky='ew')

# label for dealer
labelDealer = tkinter.Label(frameDealer, text='Dealer', fg='white', background='green')
labelDealer.grid(row=0, column=0, sticky='new')

# label for dealer points
labelDealer_Points = tkinter.IntVar()
dealer_score = 0
dealer_ace = False
tkinter.Label(frameDealer, text='Dealer', fg='white', background='green').grid(row=0, column=0)
tkinter.Label(frameDealer, textvariable=labelDealer_Points, fg='white', background='green').grid(row=1, column=0)

# Player'
# frame for player label and points
framePlayer = tkinter.Frame(frameTable, background='green')
framePlayer.grid(row=1, column=0)

# frame for player_cards
framePlayer_cards = tkinter.Frame(frameTable, background='green')
framePlayer_cards.grid(row=1, column=1, sticky='we')

# label for player
labelPlayer = tkinter.Label(framePlayer, text='Player', fg='white', background='green')
labelPlayer.grid(row=0, column=0, sticky='new')

# label for player points
labelPlayer_Points = tkinter.IntVar()
player_score = 0
player_ace = False
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
cards = []
load_cards(cards)
deck = cards
random.shuffle(deck)

# dealer/player hands:
dealer_hand = []
player_hand = []

mainWindow.mainloop()
