

""" Jag kommer att göra tavlan med hjälp av ordbok
    siffran = nycklar och den nyckeln man väljer att skriva in kommer nämna din position 
    på det sättet som det visas i respektive tavla  och initialt kommer 
    dess värden att vara tomt utrymme och sedan efter varje drag
    vi kommer att ändra värdet enligt spelarens val av drag. """


from matplotlib.pyplot import pause, table




# Här kommer jagg att behöva skriva ut den uppdaterade tavlan efter varje drag i spelet och
    #Därför kommer vi att skapa en funktion där vi kommer att definiera printtavla-funktionen
    #så att vi enkelt kan skriva ut tavlan varje gång genom att anropa den här funktionen. på det viset
    #sparar vi tid, och förenklar koden så bra som möjligt.'''


def printtavla(tavla):
            print(tavla[1] + '|' + tavla[2] + '|' + tavla[3])
            print('-------')
            print(tavla[4] + '|' + tavla[5] + '|' + tavla[6])
            print('-------')
            print(tavla[7] + '|' + tavla[8] + '|' + tavla[9])


class Spelare:
    #det kommer alltid att finnas en vinnare därför måste vi skapa en klass för player och spara informationen för att programmet sedan
    #ska kunna utav sig själv välja ut rätt vinnare med rätt information. därför har jag valt namn och poäng. anledningen till varför
    #jag har valt att ha poäng är för att de senare kommer att få bestämma hur många gånger de ska spela
        def __init__(self,namn,poäng):
            self.namn= namn
            self.poäng=poäng

def lägg_Spelare():
    pause




def Checkvinst(tavla):
        
        win = 0
        draw = -1
        running = 1
        Game = 1 
        

        if(tavla[1] == tavla[2] and tavla[2] == tavla[3] and tavla[1] != ' '):    
           Game = win
        elif(tavla[4] == tavla[5] and tavla[5] == tavla[6] and tavla[4] != ' '):
            Game = win
        elif(tavla[7] == tavla[8] and tavla[8] == tavla[9] and tavla[7] != ' '):    
            Game = win    
    #Verticalt vinst    
        elif(tavla[1] == tavla[4] and tavla[4] == tavla[7] and tavla[1] != ' '):
            Game = win    
        elif(tavla[2] == tavla[5] and tavla[5] == tavla[8] and tavla[2] != ' '):    
            Game = win    
        elif(tavla[3] == tavla[6] and tavla[6] == tavla[9] and tavla[3] != ' '):    
            Game=  win    
    #Diagonal Winning Condition    
        elif(tavla[1] == tavla[5] and tavla[5] == tavla[9] and tavla[5] != ' '):    
            Game = win    
        elif(tavla[3] == tavla[5] and tavla[5] == tavla[7] and tavla[5] != ' '):    
            Game= win    
    #Match Tie or Draw Condition    
        elif(tavla[1]!=' ' and tavla[2]!=' ' and tavla[3]!=' ' and tavla[4]!=' ' and tavla[5]!=' ' and tavla[6]!=' ' and tavla[7]!=' ' and tavla[8]!=' ' and tavla[9]!=' '):    
            Game= draw   
        else:            
            Game= running

        return Game

def play_game(tavla, player):
    running = True
    if player == 1:
        mark = "X"
    elif player == 2:
        mark = "O"

    while running:
        position = int(input("Välj din position från 1 - 9, OBS: obeservera att man börjar räkningen från högst upp i vänster!\nPosition: "))
        if position < 10 and position > 0:
            update = {position : mark}
            tavla.update(update)
            printtavla(tavla)
            running = False
        else:
            print("Något gick fel, försök igen...")
    return tavla
def main():
    tavla =     {  1: ' ' , 2: ' ' , 3: ' ' ,
                4: ' ' , 5: ' ' , 6: ' ' ,
                7: ' ' , 8: ' ' , 9: ' ' }

    board_keys = []
    for nycklar in tavla:
        board_keys.append(nycklar)

    running = 1
    player = 1

    Game = 1

    print("Tic tac toe Skapad av kungen Daniel")
    print("Första spelare är X andra kommer att vara O gör eran va nu \n")
    print("")
    printtavla(tavla)
    while Game == running:
        tavla = play_game(tavla, player)
        player +=1
        if player == 3:
            player = 1
        Game = Checkvinst(tavla)
    if Game == 0:
        player -= 1
        print(f"Player {player} won!")
    else:
        print("The game ended in a draw")
        
main()

lägg_Spelare()

