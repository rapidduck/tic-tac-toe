import random
import time

WIN_SITUATIONS = [
    [(0,0), (1,1), (2,2)],
    [(0,2), (1,1), (2,0)],
    [(0,0), (1,0), (2,0)],
    [(0,1), (1,1), (2,1)],
    [(0,2), (1,2), (2,2)],
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
]


class Game:
    """Stores gameboard info and deals with displaying and games functions."""
    def __init__(self):
        self.gameboard = [
                            [" ", " ", " "],
                            [" ", " ", " "],
                            [" ", " ", " "]
                        ]

    def display_gameboard(self):
        """Displays current gameboard."""
        print("    0   1   2 ")
        print("   ___ ___ ___")
        for index, row in enumerate(self.gameboard):
            row_print = f"{index} |"
            for cell in row:
                row_print += f" {cell} |"
            print(row_print)
            print("   --- --- ---")

    def hit_spot(self, position, sign):
        """Saves players hit in gameboard, checks if it is a valid hit and proceeds to display the gameboard
        and check if the game has not already finished."""
        x, y = position
        try:
            self.gameboard[y][x]
        except IndexError:
            print("Invalid spot. You messed up.")
            exit(69)
        else:
            if self.gameboard[y][x] != " ":
                print("Dummy, this spot is already occupied.")
                exit(69)
            self.gameboard[y][x] = sign
        self.display_gameboard()
        self.check_game_status()

    def check_game_status(self):
        """Checks if the game has resulted in a WIN/LOSE/DRAW situation."""
        for situation in WIN_SITUATIONS:
            first_char = None
            win = True
            for position in situation:
                char = self.gameboard[position[1]][position[0]]
                if char != " " and first_char is None:
                    first_char = char
                if char == " " or char != first_char and first_char != " ":
                    win = False
            if win:
                print(f"Player {first_char} has won!")
                exit(0)
        is_full = True
        for row in self.gameboard:
            for cell in row:
                if cell == " ":
                    is_full = False
        if is_full:
            print(f"Game has resulted in a draw.")
            exit()

    def computer_move(self):
        """Decides computer's next move."""
        computers_coords = (random.randint(0, 2), random.randint(0, 2))
        if self.gameboard[computers_coords[1]][computers_coords[0]] != " ":
            return self.computer_move()
        else:
            return computers_coords


def ask_for_coords():
    """Asks the user for the spot he wishes to play."""
    inputted_text = input("What spot do you want to check? Input in COLUMN-ROW format. (1-2): ")
    parts = inputted_text.split("-")
    if len(parts) != 2:
        print(f"Input the coords correctly next time.")
        exit(-1)
    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        print(f"Those ain't numbers.")
        exit(-1)
    else:
        return x, y


game = Game()
game.display_gameboard()
player1 = "X"
player2 = "O"

print(f"You are player {player1}")

while True:
    coords = ask_for_coords()
    game.hit_spot(coords, player1)
    print(f"Wait computer is thinking..")
    time.sleep(2)
    game.hit_spot(game.computer_move(), player2)