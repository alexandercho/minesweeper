from GameBoard import *
from DisplayBoard import *
from Game import *

def parse_play_game():
    play_game = input()
    while (play_game != 'y' and play_game != 'n'):
        print('Please enter y or n')
        play_game = input()
    return play_game

def parse_grid():
    print('What is the length of your square grid?')
    N = 'A'
    while (type(N) is not int()):
        N = input()
        try:
            N = int(N)
            break
        except ValueError:
            print('Please enter an integer value')

    print('How many mines are in your grid?')
    M = 'A'
    while (type(M) is not int()):
        M = input()
        try:
            M = int(M)
            break
        except ValueError:
            print('Please enter an integer value')

    return N, M

def parse_move(g):
    row, col = -1, -1
    move = None
    print('Which cell do you want to uncover? (Enter row number and column number separated by space)')
    while (not g.is_valid_move(row,col)):
        move = input()
        moves = move.split()
        if len(moves) == 2:
            try:
                row = int(moves[0]) - 1
                col = int(moves[1]) - 1
                if g.is_valid_move(row, col):
                    break
                print('Please enter a valid move.')
            except ValueError:
                print('Please enter a valid move.')
    return row, col

if __name__ == '__main__':
    print('Welcome to Minesweeper. Play a game? (y/n)')
    play_game = parse_play_game()

    while play_game == 'y':
        N, M = parse_grid()
        g = Game(N,M)
        print(str(g.displayboard))
        while not g.game_over:
            row, col = parse_move(g)
            g.play_move(row, col)
            print(str(self.displayboard))


        if g.game_won:
            print('You win!')
        else:
            print('You lost.')
            
        g.uncover_board()
        print(str(g.displayboard))
        print('Play again? (y/n)')



        play_game = parse_play_game()
