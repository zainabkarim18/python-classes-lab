class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            start_game = input("Shall we play a game? (yes/no): ").lower()
            if start_game == 'yes':
                self.run_game()
            elif start_game == 'no':
                print("Game has been stopped.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def run_game(self):
        self.reset_game()
        while self.winner is None and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()
        self.end_game()
            
    def reset_game(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: a1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move. Please try again.")

    def check_for_winner(self):
        winning_combos = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['c1', 'b2', 'a3']
        ]

        for combo in winning_combos:
            if self.board[combo[0]] and self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                self.winner = self.board[combo[0]]
                return

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and self.winner is None:
            self.tie = True

    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def end_game(self):
        while True:
            replay = input("Do you want to play again? (yes/no): ").lower()
            if replay == 'yes':
                self.run_game()
                self.reset_game()
                break
            elif replay == 'no':
                print("Thank you for playing!")
                exit() 
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
game_instance = Game()
game_instance.play_game()
