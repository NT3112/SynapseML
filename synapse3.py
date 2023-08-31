#task4
class ChessPlayer:
    def __init__(self,player,age,elo,tenacity,isboring):
        self.player=player
        self.age=age
        self.elo=elo
        self.tenacity=tenacity
        self.tournament=0

    def simulate_match(self,opp):
        diff=abs(self.elo-opp.elo)
        if diff>100:
            if self.elo>opp.elo:
                self.tournament+=1
            else:
                opp.tournament+=1
        elif 50<=diff<=100:
            r=random.randint(0,10)
            
            if self.elo>opp.elo:
                if opp.elo*r>self.elo:
                    opp.tournament=1
                else:
                    self.tournament=1
            else:
                if self.elo*r>opp.elo:
                    self.tournament=1
                else:
                    opp.tournament=1
        else:
            if diff<50:

                if self.tenacity>opp.tenacity:
                    self.tournament=1
                else:
                    opp.tournament=1
            elif self.isboring=='True' or opp.isBoring=='True':
                    self.tournament=0.5
                    opp.tournament=0.5

players = [
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)
]

for i in range(len(players)) :
    for j in range(i+1,len(players)):
        players[i].simulate_match(players[j])
        players[j].simulate_match(players[i])

for i in players:
    print(f"{i.name}\t{i.score}")       





               
                

        

             


        
