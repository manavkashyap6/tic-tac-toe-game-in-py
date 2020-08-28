#-----------gobal variable ---------------


#game board
board =["-","-","-",
        "-","-","-",
        "-","-","-"]

#game is still going 
game_still_going = True

#win or Tie
winner = None

#whos turn is it
current_player = "x"
def display_borad():
  print (board[0]+" | " + board[1]+" | "+ board[2])
  print (board[3]+" | " + board[4]+" | "+ board[5])
  print (board[6]+" | " + board[7]+" | "+ board[8])


def play_game():

 #display intial board
  display_borad()

  while game_still_going:
    handle_turn(current_player)

    check_if_game_over()

    #flip to other player 
    flip_player()

    #if game over 
  if winner == "x" or winner == "0":
    print(winner+" won.")
  elif  winner == None:
      print("tie.")




def handle_turn(player):

  print (player + "'s turn.'")

  position = input("choose a position from 1-9:")

  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("invalid input,choose a position from 1-9:")

    position = int(position) - 1

    if board [position] == "-":
      valid = True
    else:
      print ("you can't go there go again.")

  board[position] = player

  display_borad()

def check_if_game_over():
  check_for_winner()
  chech_if_tie()
  

def check_for_winner():

  global winner

  #check row
  row_winner = check_row()
  #check colunms
  colunm_winner =check_colunm()
  #check digonal
  digonal_winner = check_digonal()
  if row_winner:
    winner = row_winner
  elif colunm_winner:
    winner = colunm_winner
  elif digonal_winner:
    winner = digonal_winner
  else:
    winner= None
  return

def check_row():

  #set gobal variable
  global game_still_going

  row_1 = board[0] == board[1] == board[2] !="-"
  row_2 = board[3] == board[4] == board[5] !="-"
  row_3 = board[6] == board[7] == board[8] !="-"
  
  #if any row does have a match , flag that there is a win   
  if row_1 or row_2 or row_3:
    game_still_going = False 
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_colunm():
   #set gobal variable
  global game_still_going

  colunm_1 = board[0] == board[3] == board[6] !="-"
  colunm_2 = board[1] == board[4] == board[7] !="-"
  colunm_3 = board[2] == board[5] == board[8] !="-"
  
  #if any row does have a match , flag that there is a win   
  if colunm_1 or colunm_2 or colunm_3:
    game_still_going = False 
  if colunm_1:
    return board[0]
  elif colunm_2:
    return board[1]
  elif colunm_3:
    return board[2]
  return
  

def check_digonal():
   #set gobal variable
  global game_still_going

  digonal_1 = board[0] == board[4] == board[8] !="-"
  digonal_2 = board[2] == board[4] == board[6] !="-"
 
  
  #if any row does have a match , flag that there is a win   
  if digonal_1 or digonal_2:
    game_still_going = False 
  if digonal_1:
    return board[0]
  elif digonal_2:
    return board[2]
  return
  



def chech_if_tie():

  global game_still_going
  
  if "-" not in board:
    game_still_going = False
  
  return

def flip_player():

  #global player
  global current_player
  if current_player =="x":
    current_player = "0"
  elif current_player =="0":
    current_player = "x"
  return



play_game()























#board
#display board 
#play game
#check win 
 #check R
 #check c
 #check d
#check Tie
#flip player 
