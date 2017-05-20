import random


def reset_game():
    global board, valid_moves_played
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    valid_moves_played = 0


def print_scores(scores):
    print("The score is currently {}-{}".format(scores[1], scores[2]))


def play_again():
    play = input("Do you want to play again (y/n)? ")
    if play.lower() == 'n':
        return 0
    else:
        return 1


def check_win(board):
    text = ""
    win = 0
    size = len(board)
    for i in range(0, size):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            text = 'Horizontal win for player {}'.format(board[0][i])
            win = 1
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            text = 'Vertical win for player {}'.format(board[i][0])
            win = 1

    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != 0:
        text = 'Diagonal win for player {}'.format(board[0][0])
        win = 1
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != 0:
        text = 'Diagonal win for player {}'.format(board[0][2])
        win = 1
    return text, win


def draw_board(board):
    width = len(board)
    height = len(board)
    horizontal = " "
    for i in range(0, width):
        horizontal += "--- "
    for j in range(0, height):
        vertical = "|"
        for i in range(0, width):
            if board[i][j] == 2:
                display="O"
            elif board[i][j] == 1:
                display="X"
            else:
                display=" "
            vertical += " {} |".format(display)
        print(horizontal)
        print(vertical)
    print(horizontal)


def get_human_move():
    valid_move = 0
    while valid_move == 0:
        move = input('Player 1 enter your move [x,y]: ')
        if move[0].isdigit() == 1 and move[-1].isdigit() == 1:
            # convert input to appropriate numbers
            move_y = int(move[0])
            move_x = int(move[-1])
            move_x -= 1
            move_y -= 1
            if board[move_y][move_x] == 0:
                valid_move = 1
    return move_y, move_x


def get_cpu_move():
    valid_move = 0
    while valid_move == 0:
        move_x = random.randint(0, 2)
        move_y = random.randint(0, 2)
        if board[move_y][move_x] == 0:
            valid_move = 1
    return move_y, move_x


def main():
    global valid_moves_played
    player = 1
    player_scores = [0, 0, 0]
    game_in_progress = 1
    reset_game()
    while game_in_progress == 1:
        if player == 1:
            move_y, move_x = get_human_move()
        else:
            move_y, move_x = get_cpu_move()
        board[move_y][move_x] = player
        valid_moves_played += 1
        draw_board(board)
        text, win = check_win(board)
        if win:
            print(text)
            player_scores[player] += 1
            print_scores(player_scores)
            game_in_progress = play_again()
            reset_game()
        if valid_moves_played == 9:
            print("Stalemate.... time for a new board!")
            print_scores(player_scores)
            game_in_progress = play_again()
            reset_game()

        if player == 1:
            player = 2
        else:
            player = 1
    print("Thanks for playing - bye!")


if __name__ == '__main__':
    main()
