
# Här har jag importat vissas grejer, Såsom pause, men även player från klassen, vilket kommer ifrån en annan fil, alltilså är den 
#en slags filhantering. Men mer filhantering kommer att dyka upp senare i koden. Jag har även importat random, eftersom att 
# man kan välja att köra spelet mot en bot, som random kommer att sätta ut en ett O i tavlan

import encodings
from matplotlib.pyplot import pause, table
from Klassen import Player
import random



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





def Checkvinst(tavla):
#Självklart vill man veta vem som vann, Därför har vi skapat en funktion, med namnet Checkvinst. Den ska kolla alla sätt att vinna
# Det vill säga Vertival vinst, Diognal vinst men också draw. Sedan ska vi använda oss av denna funktionen för att se vad som har hänt
# i spelet, ifall de har vunnit, ska den kolla hur det har skett. Eller så ska den kolla ifall det ens är någon vinst. Jag har även
# gett vissa varibler såsom win, draw, running och game ett värde, som sedan kommer att spela ett större roll.
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
# Här retunerar jag spelet, för att se resultatet.

def play_game(tavla, player):
    #Plat_game är en funktion för att kunna spela spelet överhuvudtaget. Som ni har sätt har vi skapat ett tavla, men man vill kunna spela
    # Det kommer fungera så här, Som du kan se på printtavla finns det siffror på listor, Det är nycklar med andra ord. Det beskriver 
    #positoner, som ni ser är längst upp till vänster 1 och siffran som är längst ner till höger är 9. Detta kommer vi att uttnykja,
    # Man kommer att Till och början med få frågan, "Hur många är ni som ska spela?" Man kommer högst kunna välja 2 och minst kunna välja 1
    # Kör du på 1 kommer du att kopplas till en bot som du ska försöka besegra. Första spelaren är alltid X, Om du väljer att köra mot 2 
    # kommer du att möta en motståndare eller en vän som också ska lägga till sitt namn. 


    #  Här kollar det först att spelet körst igång, Sedan lägger den spelare 1 som x och spelare 2 som O, ifall det endast finns 1 spelare
    # så kommer spelare att vara X, men det kommer vi till senare 
    running = True
    if player == 1:
        mark = "X"
    elif player == 2:
        mark = "O"


#Sedan går koden vidare hit, Det ska kolla upp det genom att den ser först och främst ifall koden fortfarande än igång,
# Ifall allt har fungerat fint, vilket den ska göra så ska koden skickas till variablen pisition, Den ska be dig att nämna ett nummer,
# mellan 1 -  9 Det är alltilså de här nycklarna som tidigare nämnts. Jag har även kört ett while- loop på den för att ifall 
# spelaren inte följer reglarna det vill säga ifall positionen är högre än 9 eller mindre än 1, eller ännu värre ifall det är en boxtav som är skriven
#då ska frågan ställas igen. Rättare sagt, kommer man att få besvara frågan igen. Om allting följs till prick så kommer X/ o att sättan in i tavlan
# för att det ska visas har jag returnat tavlan här, då gör man sina drag och därefter upptateras tavlan. 
    while running:
        position = int(input("Välj din position från 1 - 9, OBS: obeservera att man börjar räkningen från högst upp i vänster!\nPosition: "))
        if position < 10 and position > 0:
            if tavla[position] == " ":
                update = {position : mark}
                tavla.update(update)
                printtavla(tavla)
                running = False
            else:
                print("Den positionen är redan tagen, försök igen...")
        else:
            print("Något gick fel, försök igen...")
    return tavla

def bot_play_game(tavla, player):
    #Här är spelet för de som vill möta en bot, Han är inte svår alls, men det är någon att köra med. Samma gäller här, den kommer
    #först och främst kolla om spelet körs, därefter kommer den att att positionera spelare 1 och 2 till X och O, Som sagt spelare 1 är alltid X
    # Och spelare 2 är O
    running = True
    if player == 1:
        mark = "X"
    elif player == 2:
        mark = "O"
# While-loopen har jag redan förklarat
    while running:
        if player ==1:
            position = int(input("Välj din position från 1 - 9, OBS: obeservera att man börjar räkningen från högst upp i vänster!\nPosition: "))
            if position < 10 and position > 0:
                if tavla[position] == " ":
                    update = {position : mark}
                    tavla.update(update)
                    printtavla(tavla)
                    running = False
                else:
                    print("Den positionen är redan tagen.")
            else:
                 print("Något gick fel, försök igen...")
        else:
            #Efterom att vi kör mot bots nu, måste spelet skilja sig ifrån när man kör mot en riktig människa
            # Jag tillåter boten att skriva upp ett random nummer från 0 - 9
            #sedan kommer nummret att felsökas, Först kommer den kollas at IF den andra ifstatsen ifall positionen är tom., 
            # Där efter. Därefter skriver den ut vilken position botten la ut i det senaste draget. Återigen är detta en while-loop, 
            # men den skriver it ut felen som botten har gjort istället gör kör botten om tills den har rätt, och det sker väldigt snabbt, det märks inte ens av.
            # Felen jag snackar om är exempelvis att botten nämner en position som redan är använd. Vanligt vis får vi som spelare ett litet meddellande, som säger att positionen är använd
            # men botten gör om det väldigt snabbt och slumpar, flertals gånger, och det märks inte ens av, som att botten inte gör något fel alls. Som förra gången så retuneras tavlan
            # i slutändan
            position = random.randint(0,9)
            if position < 10 and position > 0:
                if tavla[position] == " ":
                    print(f"The bot place their mark on position {position}.")
                    update = {position : mark}
                    tavla.update(update)
                    printtavla(tavla)
                    running = False
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

    with open ("Tic.txt", "r", encoding = "utf8") as f:
        for line in f.readlines():
            print(line)
    print("Första spelare är X andra kommer att vara O gör eran val nu \n")
    print("")
    printtavla(tavla)
    players = Player.add_players()
    while Game == running:
        if len(players) == 1:
            tavla = bot_play_game(tavla, player)
        elif len(players) == 2:
            tavla = play_game(tavla, player)
        player +=1
        if player == 3:
            player = 1
        Game = Checkvinst(tavla)
    
    if Game == -1:
        print("The game ended in a draw")
    else:
        if len(players) == 1:
            if player == 2:
                print(f"{players[0]} won!")
            elif player == 1:
                print("The bot won!")
        elif len(players) == 2:
            player -= 1
            print(f"Player {players[player]} won!")
        
main()
    