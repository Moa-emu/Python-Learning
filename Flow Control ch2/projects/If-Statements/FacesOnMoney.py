#this is exercise: 43

# It is common for images of a country’s previous leaders, or other individuals of historical significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in Table 2.1.
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the
# banknote of the entered amount. An appropriate error message should be displayed
# if no such note exists.

# here is the table:
# George Washington - $1
# Thomas Jefferson - $2
# Abraham Lincoln -$5
# Alexander Hamilton - $10
# Andrew Jackson - $20
# Ulysses S. Grant - $50
# Benjamin Franklin - $100


print('please give me a demonation of a banknote and I will tell you whos face is on the bill:')
userBankNote = int(input())
if userBankNote == 1:
    print(f'the ${userBankNote} has the face of president George Washington' )

elif userBankNote == 2:
    print(f'the ${userBankNote} has the face of president Thomas Jefferson' )

elif userBankNote == 5:
    print(f'the ${userBankNote} has the face of president Abraham Lincon' )

elif userBankNote == 10:
    print(f'the ${userBankNote} has the face of president Alexander Hamilton' )

elif userBankNote == 20:
    print(f'the ${userBankNote} has the face of president Andrew Jackson' )

elif userBankNote == 50:
    print(f'the ${userBankNote} has the face of president Ulysses S. Grant' )

elif userBankNote == 100:
    print(f'the ${userBankNote} has the face of founding father Bengamin Franklin' )


else:
    print('They do not make bills of that number')

 