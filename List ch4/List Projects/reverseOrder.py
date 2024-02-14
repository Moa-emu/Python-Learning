#This is Exercise 105: Reverse Order

# Write a program that reads integers from the user and stores them in a list. Use 0 as
# a sentinel value to mark the end of the input. Once all of the values have been read
# your program should display them (except for the 0) in reverse order, with one value
# appearing on each line.



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
    userList.sort(reverse=True)
    print(userList)




if __name__ == "__main__":
    main()