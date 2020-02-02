tup = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
num_board = [[0,0,0],[0,0,0],[0,0,0]]
num_array = [0,1,2]
winner = 0
def chance(rownum,colnum,player,board):
    '''
    Just to place value in the board.
    checking of valid moves is done in make_move function
    '''
    if player==1:
        board[rownum][colnum] = 'O'
    else:
        board[rownum][colnum] = 'X'
def check_winner(board,num_board,player):
    '''
    input: board, num_board, player number
    output: bool tuype. if output is one, then input player is winner
    '''
    for (x,y) in tup :
        if board[x][y] == '_':
            num_board[x][y] = 0
        elif board[x][y] == 'O':
            num_board[x][y] = 1
        else:
            num_board[x][y] = -1
    winner = (row_check(num_board,player))or(col_check(num_board,player))or(diag_check(num_board,player))
    return winner   
def row_check(num_board,player):
    sum = 0
    if player == 1:
        for x in num_array:
            for y in num_array:
                sum+= num_board[x][y]
            if sum==3:
                return True #i get which player has won
            sum = 0
        return False
    else:
        sum = 0
        for x in num_array:
            for y in num_array:
                sum+= num_board[x][y]
            if sum==-3:
                return True
            sum = 0
        return False
def col_check(num_board,player):
    sum = 0
    if player == 1:
        for y in num_array:
            for x in num_array:
                sum+= num_board[x][y]
            if sum==3:
                return True #i get which player has won
            sum = 0
        return False
    else:
        sum = 0
        for y in num_array:
            for x in num_array:
                sum+= num_board[x][y]
            if sum==-3:
                return True
            sum = 0
        return False
def diag_check(num_board,player):
    if player == 1:
        sum1 = num_board[0][0]+num_board[1][1]+num_board[2][2]
        sum2 = num_board[0][2]+num_board[1][1]+num_board[2][0]
        return (sum1==3)or(sum2==3)
    else:
        sum1 = num_board[0][0]+num_board[1][1]+num_board[2][2]
        sum2 = num_board[0][2]+num_board[1][1]+num_board[2][0]
        return (sum1==-3)or(sum2==-3)
def make_move(board,player):
    print(f'Chance of player {player} ')
    r=input("Enter the row at which to enter ")
    c=input("Enter the col at which to enter ")
    r = int(r)
    c = int(c)
    if board[r][c]!= '_':
        print('\nAlready moved. Make a move again \n')
        make_move(board,player)
    else:
        chance(r,c,player,board)
    if check_winner(board,num_board,player):
        print(f'player {player} is winner')
        return True
    else:
        print("Chance of other player")
        return False
def print_board(board):
    for i in num_array:
        for j in num_array:
            print(board[i][j] , end=" ")
            print(" " , end=" ")
        print("\n")
def main():
    board = [['_','_','_'],['_','_','_'],['_','_','_']]
    num_board = [[0,0,0],[0,0,0],[0,0,0]]
    play =1
    num_move = 0
    tog = -1
    win = False
    print_board(board)
    while win!=True:
        tog*=-1
        if tog == -1:
            play = 2
        else:
            play = 1
        win = make_move(board,play)
        print_board(board)
        num_move+=1
        if num_move==9:
            print("The game was a draw")
            return 
if __name__ == '__main__':
	main()