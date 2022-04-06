""" Jag kommer att göra tavlan med hjälp av ordbok
    siffran = nycklar och den nyckeln man väljer att skriva in kommer nämna din position 
    på det sättet som det visas i respektive tavla  och initialt kommer 
    dess värden att vara tomt utrymme och sedan efter varje drag
    vi kommer att ändra värdet enligt spelarens val av drag. """




Tavlan = {  '1': ' ' , '2': ' ' , '3': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                ' 7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []
for nycklar in Tavlan:
    board_keys.append(nycklar)

# Här kommer jagg att behöva skriva ut den uppdaterade tavlan efter varje drag i spelet och
    #Därför kommer vi att skapa en funktion där vi kommer att definiera printtavla-funktionen
    #så att vi enkelt kan skriva ut tavlan varje gång genom att anropa den här funktionen. på det viset
    #sparar vi tid, och förenklar koden så bra som möjligt.'''


def printtavla(tavla):
            print(tavla['1'] + '|' + tavla['2'] + '|' + tavla['3'])
            print('-----------------------------------------------')
            print(tavla['4'] + '|' + tavla['5'] + '|' + tavla['6'])
            print('-----------------------------------------------')
            print(tavla['7'] + '|' + tavla['8'] + '|' + tavla['9'])


class Player:
    #det kommer alltid att finnas en vinnare därför måste vi skapa en klass för player och spara informationen för att programmet sedan
    #ska kunna utav sig själv välja ut rätt vinnare med rätt information. därför har jag valt namn och poäng.
        def __init__(self,namn,poäng):
            self.namn= namn
            self.poäng=poäng

def add_player():
    första= input("vad är första spelarens namn")
    fpoäng = 0 
    player1 = Player(första,fpoäng)
    
