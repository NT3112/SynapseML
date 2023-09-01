import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.score = 0
    
    def simulateMatch(self, opponent):
        elo_difference = opponent.elo - self.elo
        random_factor = random.randint(1, 10)

        if elo_difference > 100:
            winner = opponent if elo_difference > 0 else self
        elif 50 <= elo_difference <= 100:
            if random_factor * self.tenacity > opponent.elo:
                winner = self
            else:
                winner = opponent
        else:
            if self.tenacity > opponent.tenacity:
                winner = self
            else:
                winner = opponent

        if self.is_boring and elo_difference <= 100:
            winner = None
        
        if winner is not None:
            winner.score += 1
            print(f"{self.name} vs {opponent.name}: {winner.name} wins")
        else:
            print(f"{self.name} vs {opponent.name}: Draw")

# Define the players
players = [
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False),
]

# Simulate the tournament
for player1 in players:
    for player2 in players:
        if player1 != player2:
            player1.simulateMatch(player2)

# Print the final table of results
print("\nFinal Results:")
for player in players:
    print(f"{player.name} - Score: {player.score}")   





               
                

        

             


        
