# This is Exercise 107

def main():
    #below will be an empty list that will contain everything the user adds
    usersList = []
    while True:
        print('Type nothing and press enter when you want to stop')
        userAdd = str(input('Please add whatever words you want they will be added to list: '))
        
        #below if the user types nothing and presses enter the loop is broken 
        if userAdd == "":
            break
        if userAdd in usersList:
            #below we will use continue to skip the current iteration and immediately start the next iteration of the loop.
            continue
        else:
            #below will add what the user typed into the list
            usersList.append(userAdd)
    
    #Below we will use a for loop to go through the userList and print them out one by one
    for i in range(0, len(usersList)):
        print(usersList[i])


if __name__ == "__main__":
    main()