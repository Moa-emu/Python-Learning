# Using Data Structures to Model Real-World Things

#- we will be showing how list and dictionaries are useful for applications like
#modeling data to represent certian things lika a chess board or tick tack toe


#In this Lesson we will be making a TICK TACK TOE BOARD
#Below will be what we will be going for

#           |         |
# 'top-l'   | 'top-M' | 'top-R'
#-----------|---------|--------------
# 'mid-l'   | 'mid-M' | 'mid-R'
#-----------|---------|--------------
# 'low-l'   | 'low-M' | 'low-R'
#           |         |          


#Below will be a dictionary that will have the key being the position and the
#value being whether it contins an X or an O
def TickTackToe():
    Board = {'top-L':'', 'top-M':'', 'top-R':'',
             'mid-L':'', 'mid-M':'', 'mid-R':'',
             'low-L':'', 'low-M':'', 'low-R':''}

    #Below will set each key value to 0 if 
    # for key in Board.keys():
    #     Board[key] = Board.setdefault(key, '0')
    return Board




#--------------------------------------------------------------------------------------------------

#Belwo will be how we actually draw the tick tack toe board with a function
def printBoard(Board):
    #think of it as value|value|value
    print(Board['top-L'] + '|' + Board['top-M'] + '|'+ Board['top-R'])
    print('-+-+-')
    print(Board['mid-L'] + '|' + Board['mid-M'] + '|'+ Board['mid-R'])
    print('-+-+-')
    print(Board['low-L'] + '|' + Board['low-M'] + '|'+ Board['low-R'])


def main():
    Board = TickTackToe()
    printBoard(Board)



if __name__ == "__main__":
    main()