import random

# Starting the game:
def start_game():
    num_players = int(input("What is the number of players? "))
    players_list = []
    for i in range(0, num_players):
        players_list.append(input(f"What is the name of the {i+1}° player? "))
    return players_list
    
# Creating the deck and randomizing cards:
def create_deck():
    deck = 4*[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    random.shuffle(deck)
    return deck

# Coding the each players move:
def player_move(player_name, deck):
    aces_count = 0
    points = 0
        
    # Iniciamos comprando duas cartas:
    for item in range(0,2):
        card = deck.pop()
        points += card 
        if card == 11:
            aces_count += 1
    
    print(f"Hi {player_name}! It's your turn!")
    print(f"You have {points} points.")
    buy_card = input("Do you wish to buy a new card? (y/n) ").lower()

    while buy_card == "y":
        card = deck.pop()
        points += card
        if card == 11:
            aces_count += 1
        
        if points > 21 and aces_count != 0:
            points -= 10
            aces_count -= 1
            print(f"Now you have {points} points")
            
        elif points > 21:
            print(f"Now you have {points} points")
            print(f"You are out of the game!")
            points = 0
            break
            
        else:
            print(f"Now you have {points} points")
  
        buy_card = input("Do you wish to buy another card? (y/n) ").lower()
    

    return [player_name, points]

# Starting the game:
players = start_game()
deck = create_deck()

round = []
for player in players:
    round.append(player_move(player, deck))

winner_points = 0
winner = "No one"
for result in round:
    if result[1] > winner_points:
        winner = result[0]
        winner_points = result[1]
    # in the case of a draw:
    elif result[1] == winner_points and result[1] > 0:
        winner = [winner]
        winner.append(result[0])
    
print(f"Congratulations! {winner} won the game with {winner_points} points!")