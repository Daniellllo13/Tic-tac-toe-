class Player:

    def __init__(self, name, wins):
        self.name = name
        self.wins = wins

    def get_name(self):
        return self.name
        
    def add_players():
        players = []
        Wins = 0
        while True:
            counter = (int(input("Hur många är ni som ska spela detta spelet"))) 
            if counter == 1 or counter == 2:
                for _ in range(counter):
                    #här loopar jag frågan så många gånger det finns spelare
                    player_name = input("eran namn:")
                    players.append(player_name)
                    Player(player_name, Wins)
                return players
            else:
                print("Dubbelkolla att ni är max 2 och minst 1 ")



