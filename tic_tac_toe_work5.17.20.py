import itertools
#Wrapping up TicTacToe - Python 3 Programming Tutorial p.14 (make it show winner) Time on video is 6:00
def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    else:
        return False


def win(current_game):
    #Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizantally! (-)")
            return True

    # Diagonal
    diags =[]
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
            print(f"Player {row[0]} is the winner Diagonally! (/)")
            return True


    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
            print(f"Player {row[0]} is the winner Diagonally! (\\)")
            return True

    # Vertical
    for col in range(len(game)):
        check =[]

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {row[0]} is the winner Diagonally! (|)")
            return True

        return False
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0: #Done
            print("This spot taken try again.") #Done
            return game_map, False #Done
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1 or 2? Error reads:", e)
        return game_map, False #Done
    except Exception as e:
        print("Something went very wrong!! Error reads:", e)
        return game_map, False  # Might change to return - game_map, False

play = True
player = [1, 2]
while play:

    game_size = int(input("What size do you want to play your Tic Tac Toe? " ))
    game = [[0 for i in range(game_size)] for i in range(game_size)]



    game_won = False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False



        while not played: #Done
            column_choice = int(input("What column do you want to play? (0, 1, 2):"))
            row_choice = int(input("What row do you want to play? (0, 1, 2):"))
            game, played = game_board(game, current_player, row_choice, column_choice)#2change needed: ,

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Thanks, come again.")
            play = False
        else:
            print("Not a vallid answer, so....")
            play = False










#game = game_board(game,just_display=True)
#game = game_board(game,player=1, row=2, column=1)
