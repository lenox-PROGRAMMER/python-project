import random

class AviatorGame:
    def __init__(self):
        self.total_collected = 0
        self.fake_win_threshold = 1000000  

    def get_multiplier(self, bet_amount):
        # Update total collected amount
        self.total_collected += bet_amount

        # Logic to rig outcome
        if self.total_collected < self.fake_win_threshold:
            
            crash_point = random.uniform(1.01, 2.0)
        else:
            # Give a huge win, reset counter
            crash_point = random.uniform(50.0, 200.0)
            self.total_collected = 0

        return crash_point

# Simulate multiple users betting
game = AviatorGame()

for i in range(1, 21):
    bet = random.randint(100, 5000)  
    result = game.get_multiplier(bet)
    print(f"User {i} bet Ksh {bet}, plane crashed at {result:.2f}x")
