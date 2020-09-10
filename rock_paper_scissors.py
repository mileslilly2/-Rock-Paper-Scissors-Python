import random

def main():
    print("Enter your name:")
    name = input()
    print("Hello,", name)
    info = get_player_score(name)
    play(info)

def get_player_score(name):

    text = open("rating.txt", 'r') # for this part to work you will have to create a file of format "name score\n"
    score = 0
    for line in text:
        line = line.split()
        if name == line[0]:
            score = int(line[1])
            info = {"player": name, "score": score }
            return info
        else:
            info = {"player": name, "score": 0 }
            return info

def play(info): 
       
    winning_cases = { #the winning cases for each move are stored a values for each key
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}   

    move_select = input().split(",")
    default_moves = ["rock", "paper", "scissors"]
    if not move_select[0]:
        move_select = default_moves
    print("Okay, let's start!")
    while True:
        player_move = input()
        if player_move == "!rating":
            print("Your rating", info['score'])
            continue
        elif player_move == "!exit":
            print("Bye!")
            break
        elif player_move not in move_select:
            print("Invalid input")
            continue   
        computer_move = random.choice(move_select)
        if computer_move in winning_cases[player_move]:
            info['score'] += 100
            print("Well done. The computer chose", computer_move, "and failed")
        elif computer_move == player_move:
            info['score'] += 50
            print("There is a draw (" + computer_move +")")
        elif player_move in winning_cases[computer_move]:
            print("Sorry, but the computer chose", computer_move)


if __name__ == "__main__":
    main()