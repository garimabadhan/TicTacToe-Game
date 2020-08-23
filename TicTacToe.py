# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:27:34 2020

@author: Garima
"""
import itertools

def game_board(game_map, player = 0, row = 0, column= 0, just_display = False):
    try:
        if game_map[row][column] != 0:
            print("This position is already occupied! Choose another")
            return game_map, False
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count,row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("wrong input",e)
        return game_map, False
    except Exception as e:
        print("Something Went Wrong!!", e)
        return game_map, False
   


def win(current_game):
    def allsame(l):
         if(l.count(l[0])== len(l) and l[0]!=0):
             return True
         else:
             return False
        
    #Horizontally
    for row in game:
        print(row)
        if allsame(row):
            print(f"Player {row[0]} is the winner horizontally(-)")
            return True
    #Diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if allsame(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    diags = []
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])      
    if allsame(diags):
        print(f"Player {diags[0]} is the winner diagonally(/)")
        return True
    #Vertically    
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if allsame(check):
            print(f"Player {check[0]} is the winner vertically(|)")
            return True
    return False
    
#win(game)       
play = True
player = [1,2]
while play:
    game_size = int(input("What size of Tic Tac Tie?: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False
        
        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2): "))
            row_choice = int(input("What row do you want to play? (0,1,2): "))
            game, played = game_board(game,current_player,row_choice,column_choice)
                
        if win(game):
            game_won = True
            again = input("The game is over! Do you want to play again? (y/n): ")
            if again.lower() == "y":
                print("Restarting.....")
            elif again.lower() == "n":
                print("Byeeeeee.......")
                play = False
            else:
                print("Not a valid answer! see you later")
                play = False
            
            
        