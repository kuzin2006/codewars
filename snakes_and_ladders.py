# https://www.codewars.com/kata/snakes-and-ladders-1/train/python


class SnakesLadders():

    def __init__(self):
        # gaming board description
        # describes cells with ladder bottoms and snake heads
        # cell: points_to
        self.board = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            16: 6,
            21: 42,
            28: 84,
            36: 44,
            46: 25,
            49: 11,
            51: 67,
            62: 19,
            64: 60,
            71: 91,
            74: 53,
            78: 98,
            87: 94,
            89: 68,
            92: 88,
            95: 75,
            99: 80,
        }

        # False - 1st player, True - second
        self.moves = False

        # players positions
        # 1.  There are two players and both start off the board on square 0.
        self.positions = [0, 0]

    def play(self, die1, die2):
        if 100 in self.positions:
            # Return Game over! if a player has won and another player tries to play.
            return "Game over!"
        else:
            self.positions[self.moves] += die1 + die2

            # 7.  Land exactly on the last square to win. The first person to reach the highest square on the board wins.
            #     But there's a twist! If you roll too high, your player "bounces" off the last square and moves back.
            if self.positions[self.moves] > 100:
                self.positions[self.moves] = 200 - self.positions[self.moves]

            # check snakes and ladders
            if self.positions[self.moves] in self.board.keys():
                self.positions[self.moves] = self.board[self.positions[self.moves]]

            # 4.  If the value of both die are the same then that player will have another go.
            if die1 != die2:
                # Return Player n Wins!. Where n is winning player that has
                # landed on square 100 without any remainding moves left.
                if 100 in self.positions:
                    return f"Player {self.positions.index(100) + 1} Wins!"
                else:
                    self.moves = not self.moves
                    # Otherwise return Player n is on square x. Where n is the current player
                    # and x is the square they are currently on.
                    return f"Player {int(not self.moves) + 1} is on square {self.positions[not self.moves]}"

            else:
                return f"Player {int(self.moves) + 1} is on square {self.positions[self.moves]}"


game = SnakesLadders()

print(game.play(1, 1))
print(game.play(1, 5))
print(game.play(6, 2))
print(game.play(1, 1))