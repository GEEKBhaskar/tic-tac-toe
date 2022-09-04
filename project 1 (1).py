#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


test_board = ['#','x','o','x','o','x','o','x','o','x']
display_board(test_board)


# In[3]:


def player_input():
     '''
     OUTPUT = (player 1 marker,player 2 marker)
     
     '''
     marker = ''
     while marker != 'x' or marker != 'o':
        marker = input("player 1: choose x or o: ").upper()
        if marker == 'x':
            return('x','o')
        else:
            return('o','x')


# In[4]:


player1_marker,player2_marker = player_input()


# In[5]:


def place_marker(board, marker, position):
       board[position] = marker


# In[6]:


test_board


# In[7]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[8]:


def win_check(board,mark):
    return((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))
           


# In[9]:


display_board(test_board)
win_check(test_board,'x')


# In[10]:


import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player1'
    else:
        return 'player2'


# In[11]:


def space_check(board,position):
    return board[position] == ' '


# In[12]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        return True


# In[13]:


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9) '))
    return position 


# In[14]:


def replay():
        choice = input("play again? Enter yes or no")
        return choice == 'yes'


# In[18]:


print('welcome to tic tac toe!')
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('ready to play? y or n ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)           
        
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 2 has won!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'player 1'
    if not replay():
        break


# In[ ]:




