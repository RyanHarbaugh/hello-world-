#excercise24
#Ask the user what size game board they want to draw, 
# and draw it for them to the screen using Python’s print statement.

#take input from user on board size

def print_board():
    size = int(input("Enter the size of the game board"))
    x = 1
    while x <= size:
            print(" ---  "*size + "\n" + "|   | "*size)
            x += 1
    print(" ---  "*size)
    
if __name__ == "__main__":
  print_board()
  input()

