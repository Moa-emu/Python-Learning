#This is exercise 104

# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the user enters 0. Then it should display
# all of the values entered by the user (except for the 0) in order from smallest to largest,
# with one value appearing on each line. Use either the sort method or the sorted
# function to sort the list.

#Below will be the function that will allow us to finish the exercise
def main():
    #below will be an empty list that we will add things to
    userList = []

    while True:
        
        #below will be how we ask the user 
        print('Type 0 when you are done')
        askUser = int(input('keep entering values that will be added to a list:'))
        
        #Below will be the condition to break the loop
        if askUser == 0:
            break
        else:
            userList.append(askUser)

    
    #below will sort the users list
    userList.sort()
    print(userList)

        




if __name__ == "__main__":
    main()
