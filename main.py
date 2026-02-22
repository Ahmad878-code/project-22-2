'''We will make the board using dictionary
 in which keys will be location(i.e : top-right, mid-left etc.) and initially it's value will be 
 empty space and then after every move we will change the value according to
 player's choice of move.'''

theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theboard:
    board_keys.append(key)

    '''We will have to print the updated move after every move in the game
    and thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

      turn = 'X'
      count = 0

      while True:

            printBoard(theboard)
            print("It's your turn, " + turn + ". Move to which place?")

            move = input()

            if move not in theboard:
                  print("Invalid move. Try again.")
                  continue

            if theboard[move] == ' ' :
                    theboard[move] = turn
                    count += 1
            else:
                  print("That place is already filled.\nMove to which place?")
                  continue

            if count >= 5:

                  if theboard['7'] == theboard['8'] == theboard['9'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")                
                        break

                  elif theboard['4'] == theboard['5'] == theboard['6'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

                  elif theboard['1'] == theboard['2'] == theboard['3'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

                  elif theboard['1'] == theboard['4'] == theboard['7'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

                  elif theboard['2'] == theboard['5'] == theboard['8'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

                  elif theboard['3'] == theboard['6'] == theboard['9'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

                  elif theboard['7'] == theboard['5'] == theboard['3'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

                  elif theboard['1'] == theboard['5'] == theboard['9'] != ' ':
                        printBoard(theboard)
                        print("\nGame Over.\n")                
                        print(" **** " + turn + " won. ****")
                        break

            if count == 9:
                    printBoard(theboard)
                    print("\nGame Over.\n")
                    print("It's a Tie!!")
                    break

            if turn == 'X':
                  turn = 'O'
            else:
                  turn = 'X'


      restart = input("Do you want to play again? (y/n)")

      if restart == "y" or restart == "Y":
            for key in board_keys:
                  theboard[key] = " "
            game()


if __name__ == "__main__":
      game()