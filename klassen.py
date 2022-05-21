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
            counter = input("Hur många är ni som ska spela detta spelet")
            try:
                int(counter)
            except ValueError:
                print("försök igen")
                continue
            if int(counter) == 1 or int(counter) == 2:
                break

        for _ in range (int(counter)):
            "here I loop the question as many times as there are players"
            player_name = input("eran namn:")
            players.append(player_name)
            Player(player_name, Wins)
        return players
            



