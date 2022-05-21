


from klassen import Player
import random






def print_board(board):
            """ It is the board that is going to be recalled for every steps that is taken in this game. wwhy? it will be easier and faster
         Args:
        board (_any_): it makes it posible to use it as the name of the list.
            """
    
            print(board[1] + '|' + board[2] + '|' + board[3])
            print('-------')
            print(board[4] + '|' + board[5] + '|' + board[6])
            print('-------')
            print(board[7] + '|' + board[8] + '|' + board[9])





def Checkwin(board):
        """ This function will check who won, in vertical and diagonal it will also check if the game is ended in draw
     Args:
        board (_any_): it makes it posible to use it as the name of the list.
        """
        win = 0
        draw = -1
        running = 1
        Game = 1 
        

        if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):   
           Game = win
        elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
            Game = win
        elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
            Game = win    
    #Verticalt vinst    
        elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
            Game = win    
        elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
            Game = win    
        elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
            Game=  win    
    #Diagonal Winning Condition    
        elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
            Game = win    
        elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
            Game= win    
    #Match Tie or Draw Condition    
        elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
            Game= draw   
        else:            
            Game= running

        return Game


def play_game(board, player,):
    """This will be the whole game, or at least the funtioction that will allow you to make steps at all.

    Args:
        board (any): _this will allow us to use the the the variable in this function.
        player (any): same thing here, this will allow us to use the variable in this function

    Returns:
        This funtiocs is really the whole game, it will ask you where you want to place your mark,  what your name is, but it will aslo check if 
        it is okay for you to mark the posistion, or if it is taken
    """
    running = True
    if player == 1: 
        mark = "X"
    elif player == 2:
        mark = "O"
    while running:
        while True:
            position = input("Välj din position från 1 - 9, OBS: obeservera att man börjar räkningen från högst upp i vänster!\nPosition: ")
            try:
                int(position)
            except ValueError:
                print("försök igen")
                continue
            if int(position) < 10 and int(position) > 0:
                break
            print("försök igen")

        if board[int(position)] == " ":
            update = {int(position) : mark}
            board.update(update)
            print_board(board)
            running = False
        else:
            print("Den positionen är redan tagen, försök igen...")

    return board
def bot_play_game(board, player):
    """Sometimes you are alone, that is why we have created a bot in this function

    Args:
        board (any): Allows us again to use the variable
        player (any): Same thing as upper.

    Returns:
        _type_: it will return a decent bot, that will join you for some fun.
    """

    running = True
    if player == 1:
        mark = "X"
        
    elif player == 2:
        mark = "O"
        

    while running:
        if player == 1:
            while True:
                position = input("Välj din position från 1 - 9, OBS: obeservera att man börjar räkningen från högst upp i vänster!\nPosition: ")
                try:
                    int(position)
                except ValueError:
                    print("försök igen")
                    continue
                if int(position) < 10 and int(position) > 0:
                    break
                print("försök igen")

            if board[int(position)] == " ":
                update = {int(position) : mark}
                board.update(update)
                print_board(board)
                running = False
            else:
                print("Den positionen är redan tagen, försök igen...")
        else:
            
            position = random.randint(0,9)
            "Will make the bot to choose a number between 0 and 9"
            if position < 10 and position > 0:
                if board[position] == " ":
                    print(f"The bot place their mark on position {position}.")
                    "Will print out where the bot putted his mark, becuse it seems really akward if the text is not there"
                    update = {position : mark}
                    board.update(update)
                    print_board(board)
                    running = False
    return board
def main():
    """This is the main, the final function. Here is where we are going to set up everything, put everything in right place
    and make the game playable
    """


    "this is the board and the numbers inside of it is keys, 1 - 9 that is really the posistion that you can choose between"
    board =   {  1: ' ' , 2: ' ' , 3: ' ' ,
                4: ' ' , 5: ' ' , 6: ' ' ,
                7: ' ' , 8: ' ' , 9: ' ' }
                

    board_keys = []
    for keys in board:
        board_keys.append(keys)


    running = 1
    player = 1

    Game = 1

    with open ("Tic.txt", "r", encoding = "utf8") as f:
        for line in f.readlines():
            print(line)
        "file management, it will show a text in begining saying this tic tac toe is created by the king Daniel but in swedish"

    print("Första spelare är X andra kommer att vara O gör eran val nu \n")
    print("")
    print_board(board)
    players = Player.add_players()
    "add_players is an list that contatin the players name, and now i make the verbitial become the name of the choosen names that players have wrote by themself"
    while Game == running:
        if len(players) == 1:
            board = bot_play_game(board, player)
        elif len(players) == 2:
            board = play_game(board, player)
        player +=1
        if player == 3:
            player = 1
        Game = Checkwin(board)
    
    if Game == -1:
        print("The game ended in a draw")
    else:
        if len(players) == 1:
            if player == 2:
                print(f"{players[0]} won!")
            elif player == 1:
                print("The bot won!")
        elif len(players) == 2:
            player -= 2
            print(f"Player {players[player]} won!")
        
main()
    

    